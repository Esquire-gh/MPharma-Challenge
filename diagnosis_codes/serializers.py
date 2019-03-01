from rest_framework import serializers
from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('id',
                  'category_code', 
                  'diagnosis_code',
                  'full_code',
                  'abbreviated_description',
                  'full_description',
                  'category_title')
