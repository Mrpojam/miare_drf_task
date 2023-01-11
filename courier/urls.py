from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('courier', views.CourierView)
router.register('income', views.IncomeView)

urlpatterns = [
    path('v1/', include(router.urls)), 
]