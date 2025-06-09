from django.urls import path
from .views import ribbon_create, paint_create, template_create, products

urlpatterns = [
    path('ribbon_create/', ribbon_create, name='ribbon_create'),
    path('', products, name='products'),
    path('paint_create/', paint_create, name='paint_create'),
    path('template_create/', template_create, name='template_create')
]