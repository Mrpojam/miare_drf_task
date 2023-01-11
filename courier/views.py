from django.shortcuts import render
from rest_framework import viewsets
from .models import Courier, Income
from .serializer import CourierSerializer, IncomeSerializer

# Create your views here.
class CourierView(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    seriazer_class = CourierSerializer

class IncomeView(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer