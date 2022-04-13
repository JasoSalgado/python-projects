# src/main/base/admin.py
# Django modules
from django.contrib import admin

# My modules
from .models import Task

admin.site.register(Task)

