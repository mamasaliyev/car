from rest_framework import serializers
from .models import Logo, Car, Contract


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['title','description','image']


class CarSerializer(serializers.ModelSerializer):
    logo = LogoSerializer()

    class Meta:
        model = Car
        fields = ['title', 'description', 'km', 'year', 'price', 'color', 'order', 'image', 'logo']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['month', 'year']
