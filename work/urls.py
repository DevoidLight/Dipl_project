from django.urls import path
from .views import work, endprint

urlpatterns = [
    path('', work, name='work'),
    path('end/<int:order_id>', endprint, name='endprint'),
]