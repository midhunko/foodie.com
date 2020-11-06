from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('pasta_listing/', views.pasta, name='pasta'),
    path('cart/', views.showcart, name='showcart'),
    path('cart/delete/<int:item>/', views.delete_item, name='delete_item'),
    path('cart/delete/<int:item>/yes/', views.delete_confirm, name='delete_confirm'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('added_to_cart/<int:pro>/', views.addtocart, name='addtocart'),
    path('order_placed/', views.order_placed, name='order_placed'),
    path('reviews/', views.review, name='review'),
    path('add_review/', views.add_review, name='add_review'),
]
