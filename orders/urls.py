from django.urls import path
from .views import home, create, orders

urlpatterns = [
    path('', home),
    path('orders/create/', create, name='create'),
    path('orders/', orders, name='orders')
]