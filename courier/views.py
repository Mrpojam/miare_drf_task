from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Courier, Income
from .serializer import CourierSerializer, IncomeSerializer, IncomeForDaySerializer


# Create your views here.
class CourierView(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class IncomeView(APIView):
    """
    List all incomes, or create a new incomes.
    """
    def get(self, request, format=None):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)

        if serializer.is_valid():
            try:
                income = Income.objects.get(courier = request.data.get("courier"), Date = request.data.get("Date"))
                serializer = IncomeSerializer(income, data=serializer.data)
            except:
                serializer.create(serializer.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
