from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.product_list,
        name='product_list'
    ),

    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'increase/<int:product_id>/',
        views.increase_quantity,
        name='increase_quantity'
    ),

    path(
        'decrease/<int:product_id>/',
        views.decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'remove/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    # Registration
    path(
        'register/',
        views.register,
        name='register'
    ),

    # Login
    path(
        'login/',
        views.user_login,
        name='login'
    ),

    # Logout
    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),
]