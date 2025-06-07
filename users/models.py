from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('director', 'Директор'),
        ('printer', 'Печатник'),
        ('gluer', 'Клейщик страз'),
        ('manager', 'Менеджер по заказам'),
        ('packer', 'Упаковщик'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    phone = models.CharField(max_length=20, blank=True)