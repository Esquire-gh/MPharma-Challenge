from django.contrib import admin
from .models import DiagnosisCode, Category
# Register your models here.

admin.site.register(DiagnosisCode)
admin.site.register(Category)