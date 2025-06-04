from django.urls import path
from .views import work

urlpatterns = [
    path('', work, name='work')
]