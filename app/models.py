from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import integer_validator
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    image = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    class Color(models.TextChoices):
        WHITE = 'WHITE'
        BLACK = 'BLACK'
        BLUE = 'BLUE'
        YELLOW = 'YELLOW'
        GREEN = 'GREEN'
        RED = 'RED'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product/', null=True, blank=True)
    image5 = models.ImageField(upload_to='product/', null=True, blank=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    choice = models.CharField(max_length=55, choices=Color.choices, default=Color.WHITE)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField()
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE, related_name='products',
                             related_query_name='product')

    def __str__(self):
        return self.title


"""Models for Blog"""


class WishList(models.Model):
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE,
                             related_name='wishlist')  # ko'p wishlarga bitta user
    product = models.ManyToManyField(Product,
                                     related_name='wishlist')  # ko'p productlarga ko'p wishlist


class Cart(models.Model):
    user = models.ForeignKey(to='app.User',
                             on_delete=models.CASCADE,
                             related_name='Cart')
    products = models.ManyToManyField(Product,
                                      through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    author = models.ForeignKey(to='app.User',
                               on_delete=models.CASCADE,
                               related_name='blogs')


class Post(BaseModel):
    message = models.TextField()
    user = models.ForeignKey(to='app.User',
                             on_delete=models.CASCADE,
                             related_name='posts',
                             related_query_name='post')


class Feedback(models.Model):
    name = models.CharField(max_length=155, null=True)
    email = models.CharField(default='none', null=False, max_length=155)
    subject = models.CharField(max_length=155, null=True)
    feed = models.TextField(null=True)

    def __str__(self):
        return self.email


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a user with the given email and password
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a superuser with the given email and password
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=155, unique=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25,
                                    validators=[integer_validator],
                                    null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(to='auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.id}, {self.user}'
