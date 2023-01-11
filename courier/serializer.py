from rest_framework import serializers
from .models import Courier, Income

class CourierSerializer(serializers.ModelSerializer):
    model = Courier
    fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    model = Income
    fields = '__all__'