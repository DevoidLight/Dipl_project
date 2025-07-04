from django.db import models
from products.models import Ribbons, Paints, Tempaltes
from users.models import User

# Create your models here.
class Orders(models.Model):
    STATUS_CHOICES = (
        ('accept', 'Принят'),
        ('paid', 'Оплачен'),
        ('printing', 'Печать'),
        ('gluing', 'Клейка страз'),
        ('packing', 'Упаковка'),
        ('done', 'Завершен'),
    )
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='managed_orders')
    printer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                blank=True, related_name='printed_orders')
    gluer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                              blank=True, related_name='glued_orders')
    packer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               blank=True, related_name='packed_orders')
    ribbon = models.ForeignKey(Ribbons, on_delete=models.CASCADE, related_name='orders')
    paint = models.ForeignKey(Paints, on_delete=models.CASCADE, related_name='orders')
    template = models.ForeignKey(Tempaltes, on_delete=models.CASCADE, related_name='orders')
    class_list = models.TextField()
    teacher_name = models.CharField(max_length=128)
    deploy = models.DateField()
    school = models.CharField(max_length=128)
    class_number = models.CharField(max_length=24)
    client_phone = models.CharField(max_length=20)
    count = models.IntegerField(null=True, blank=True)
    rhinestones = models.BooleanField(default=False)
    count_rhinestones = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='accept')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['deploy']