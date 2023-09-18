from django.urls import path, include
from .import  views
app_name='cart'

urlpatterns = [
    path('', views.cart_detail,name='cart_detail'),
    path('cart/add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart/remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('cart/full_remove/<int:product_id>/',views.full_remove,name='full_remove')
     ]