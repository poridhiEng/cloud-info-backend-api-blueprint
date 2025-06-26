from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('enrollments/', views.EnrollmentView.as_view(), name='enrollment-list'),
    path('enrollments/<uuid:pk>/', views.EnrollmentDetailView.as_view(), name='enrollment-detail'),
]
