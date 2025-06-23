from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('price-plan/', views.PricePlanList.as_view(), name='priceplan-list'),
    path('price-plan/<uuid:pk>/', views.PricePlanDetail.as_view(), name='priceplan-detail'),
    path('get-price/<uuid:pk>/', views.GetPriceByPlanId.as_view(), name='get-price'),
]
