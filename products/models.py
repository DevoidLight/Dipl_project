from django.db import models

# Create your models here.
class Ribbons(models.Model):
    color = models.CharField(max_length=48)
    is_active = models.BooleanField(default=True)
    length = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.color


class Paints(models.Model):
    color = models.CharField(max_length=48)
    is_active = models.BooleanField(default=True)
    length = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.color

class Tempaltes(models.Model):
    name = models.CharField(max_length=48)
    image = models.ImageField(upload_to='products/templates')

    def __str__(self):
        return self.name