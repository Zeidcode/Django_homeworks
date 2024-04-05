from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list, name='client_list'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('ordered_products/', views.ordered_products, name='ordered_products'),
]
