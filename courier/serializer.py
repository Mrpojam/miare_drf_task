from rest_framework import serializers
from .models import Courier, Income

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
    
    def update(self, instance, validated_data):
        if (validated_data.get("type") == "D"):
            instance.value = instance.value - validated_data.get("value", instance.value) 
        else:    
            instance.value = instance.value + validated_data.get("value", instance.value)
        instance.save()
        return instance


class IncomeForDaySerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 160)
    last_name = serializers.CharField(max_length = 160)
    date = serializers.DateField()
    income = serializers.IntegerField()