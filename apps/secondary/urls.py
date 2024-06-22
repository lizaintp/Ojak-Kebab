from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('blog/', views.blog, name = 'blog'),
    path('blog_detail/<int:id>/', views.blog_detail, name = 'blog_detail'),
    path('cart', views.cart, name = 'cart'),
    path('gallery', views.gallery, name = 'gallery'),
    path('menu', views.menu, name = 'menu'),
    path('product', views.product, name = 'product'),
    path('reservation', views.reservation, name = 'reservation'),
    path('shop', views.shop, name = 'shop'),
]

