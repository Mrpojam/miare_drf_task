from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Courier, Income
from .serializer import CourierSerializer, IncomeSerializer, IncomeForWeekSerializer
from django.db.models import Sum

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
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)

        Date = request.data.get("Date")
        courier = request.data.get("courier")
        type = request.data.get("type")
        value = request.data.get("value")

        if serializer.is_valid():
            try:
                income = Income.objects.get(courier = courier, Date = Date)
                serializer = IncomeSerializer(income, data=serializer.data)
            except Income.DoesNotExist:
                pass
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeForWeekView(APIView):
    """
    Get incomes of a courier per week
    """
    def post(self, request, format=None):
        data = request.data
        courier = data.get("courier")
        all_income = Income.objects.filter(courier = courier, Date__range=[data.get("start"), data.get("end")]).aggregate(Sum('value'))
        dic = [{
            'courier': courier,
            'start_date': data.get("start"),
            'end_date': data.get("end"),
            'income': all_income['value__sum']
        }]
        serializer = IncomeForWeekSerializer(dic, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)