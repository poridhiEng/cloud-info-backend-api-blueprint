from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('PricePlan.urls')),
    path('api/v1/', include('Machine.urls')),
    path('api/v1/', include('Enrollment.urls')),
]
