from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/create/', views.create, name='create'),
    path('orders/', views.orders, name='orders'),
    path('director_report/', views.director_report, name='director_report'),
    path('order/<int:pk>/edit/', views.order_edit, name='edit'),
    path('order/<int:pk>/delete/', views.order_delete, name='delete'),
]