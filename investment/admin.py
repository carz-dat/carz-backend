from django.contrib import admin
from .models import Make, CarModel, Car, Expense
from django.db.models import Sum
# Register your models here.


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'make', 'name', 'engine_type', 'year_made'
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'model', 'date_of_purchase', 'vin_code',
        'date_of_sell', 'shipment_fee', 'auction_fee', 'car_url', 'pictures', 'repair_cost', 'total_expense'
    ]

    def repair_cost(self, obj):
        return f"{obj.car.aggregate(Sum('price'))['price__sum']} USD" or "0 USD"

    def total_expense(self, obj):
        print(obj.car.aggregate(Sum('price'))['price__sum'])
        if obj.car.aggregate(Sum('price'))['price__sum'] == None:
            return f"{obj.shipment_fee + obj.auction_fee} USD"
        return f"{obj.car.aggregate(Sum('price'))['price__sum'] + obj.shipment_fee + obj.auction_fee} USD"


@admin.register(Expense)
class ExpensesModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'type', 'currency', 'price', 'car'
    ]
