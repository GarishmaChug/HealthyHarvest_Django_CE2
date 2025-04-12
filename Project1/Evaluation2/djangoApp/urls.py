from django.urls import path
from . import views



urlpatterns = [
    path('' , views.home_view,name='home'),

    path('all' , views.all_view,name='all'),
    

    path('beauty', views.beauty_view, name='beauty'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # path('all' , views.all_view,name='all'),
    path('snacks' , views.snacks_view,name='snacks'),
    # path('pharmacy' , views.pharmacy_view,name='pharmacy'),


   



    path('pharmacy', views.pharmacy_view, name='pharmacy'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # path('fruits' , views.fruits_view,name='fruits'),
    
    path('fruits', views.fruits_view, name='fruits'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),






    path('all', views.all_view, name='all_products'),
#     path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),


# path('cart/', views.cart_detail, name='cart_detail'),
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]