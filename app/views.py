from rest_framework.viewsets import ModelViewSet

from app.models import Category, Product, Order, Comment, WishList, Cart, CartItem, OrderItem, Blog, Feedback, Post, \
    UserManager
from app.permission import IsAuthorReadOnlyPermission
from app.serializer import CategorySerializer, ProductSerializer, OrderSerializer, CommentSerializer, \
    WishlistSerializer, CartItemSerializer, OrderItemSerializer, BlogSerializer, FeedbackSerializer, PostSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class WishlistView(ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer


class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CommentSerializer


class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorReadOnlyPermission)


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
