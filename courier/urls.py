from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('courier', views.CourierView)

urlpatterns = [
    path('', include(router.urls)), 
    path('income/', views.IncomeView.as_view(), name="income"),
    path('income/week', views.IncomeForWeekView.as_view(), name="weekincome")
]