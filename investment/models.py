from django.db import models
from django.db.models import Sum

# Create your models here.

CURRENCY = (
    ('USD', 'USD'),
    ('GEL', 'GEL')
)

CHOICES = (
    ('PRT', 'Parts'),
    ('LBR', 'Labor'),
    ('MSC', 'Miscellaneous')
)

class Make(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255, null=True, blank=True)
    year_made = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.name} {self.engine_type} {self.year_made}"


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    description = description = models.TextField(
        max_length=500, blank=True, null=True)
    year_made = models.CharField(max_length=255, null=True, blank=True)
    date_of_purchase = models.DateField(null=True, blank=True)
    date_of_sell = models.DateField(null=True, blank=True)
    currency = models.CharField(
        max_length=20, choices=CURRENCY, null=True, blank=True)
    shipment_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    auction_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    pictures = models.ImageField(upload_to='cars/', blank=True, null=True)
    car_url = models.URLField(blank=True, null=True)
    vin_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.model.make} {self.model.name} {self.year_made}"



class Expense(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=CHOICES)
    currency = models.CharField(max_length=20, choices=CURRENCY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, related_name="car", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car.model} {self.name} {self.price}{self.currency}"
    
    