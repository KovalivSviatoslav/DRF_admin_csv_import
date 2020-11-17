from django.db import models


# Create your models here.
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    created_at = models.DateField(default=timezone.now)
    order = models.OneToOneField('Order', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    product_name = models.CharField(max_length=260)
    created_at = models.DateField()

    def __str__(self):
        return self.product_name
