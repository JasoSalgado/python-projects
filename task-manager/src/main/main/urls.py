# src/main/main/urls.py
# Django modules
from django.contrib import admin
from django.urls import path, include

# My modules

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
