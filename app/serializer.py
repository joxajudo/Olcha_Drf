from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from app.models import Category, Product, Order, OrderItem, WishList, Cart, CartItem, User, UserManager, Post, \
    Blog, Comment, Feedback


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductSerializer(ModelSerializer):
    # user = serializers.IntegerField(widget=serializers.HiddenField(), required=False)

    class Meta:
        model = Product
        exclude = ()


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = WishList
        exclude = ()


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        exclude = ()


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ()


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ()


class OrderSerializer(ModelSerializer):
    # Serialize the related products through OrderItemSerializer
    products = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        exclude = ()


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ()


class UserMangerSerializer(ModelSerializer):
    class Meta:
        model = UserManager
        exclude = ()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class CommentSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        exclude = ()


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ()
