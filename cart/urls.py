from django.urls import path
from cart import views
urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),

    
   path('product/<int:id>/', views.product_detail, name='product_detail'),

   path('checkout/', views.checkout, name='checkout'),   
]