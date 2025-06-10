from django.urls import path
from .views import home, create, orders, director_report

urlpatterns = [
    path('', home, name='home'),
    path('orders/create/', create, name='create'),
    path('orders/', orders, name='orders'),
    path('director_report/', director_report, name='director_report')
]