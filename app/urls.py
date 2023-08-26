from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import ProductView, CategoryView, OrderView, WishlistView, CartView, OrderItemView, CommentView, \
    BlogView, PostView, FeedbackView, CartItemView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('product', ProductView)
router.register('wishlist', WishlistView)
router.register('cart', CartView)
router.register('cartItem', CartItemView)
router.register('order', OrderView)
router.register('orderItem', OrderItemView)
router.register('comment', CommentView)
router.register('blog', BlogView)
router.register('post', PostView)
router.register('feedback', FeedbackView)

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', login_api, name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]

