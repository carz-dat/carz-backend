from rest_framework import serializers
from .models import Car, CarModel, Make

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'

    def create(self, validated_data):
        return Make.objects.create(**validated_data)


class CarModelSerializer(serializers.ModelSerializer):
    make = MakeSerializer()

    class Meta:
        model = CarModel
        fields = ["id", "make", "name", "engine_type"]


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    year_made = serializers.DateField(
        format="%Y-%m-%d")
    date_of_purchase = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True)
    date_of_sell = serializers.DateTimeField(
        format="%Y-%m-%d", read_only=True)
    shipment_fee = serializers.DecimalField(max_digits=10, decimal_places=2)
    auction_fee = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Car
        fields = ["id", "model", "year_made",
                  "shipment_fee", "auction_fee", "pictures", "car_url"]
        read_only_fields = ['date_of_sell', 'date_of_purchase']
