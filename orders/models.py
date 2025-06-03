from django.db import models
from products.models import Ribbons, Paints, Tempaltes

# Create your models here.
class Orders(models.Model):
    ribbon = models.ForeignKey(Ribbons, on_delete=models.CASCADE, related_name='orders')
    paint = models.ForeignKey(Paints, on_delete=models.CASCADE, related_name='orders')
    template = models.ForeignKey(Tempaltes, on_delete=models.CASCADE, related_name='orders')
    class_list = models.FileField()
    teacher_name = models.CharField(max_length=128)
    deploy = models.DateField()
    school = models.CharField(max_length=128)
    class_number = models.CharField(max_length=24)