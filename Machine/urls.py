from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.MachineList.as_view(), name='machine-list'),
    path('machine/<uuid:pk>/', views.MachineDetail.as_view(), name='machine-detail'),
]
