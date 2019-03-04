from rest_framework import serializers
from .models import DiagnosisCode, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('version', 'code', 'title')


class DiagnosisCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisCode
        fields = ('id',
                  'category',
                  'diagnosis_code',
                  'full_code',
                  'abbreviated_description',
                  'full_description')
