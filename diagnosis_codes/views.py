from rest_framework import generics

from diagnosis_codes.models import Code
from diagnosis_codes.serializers import CodeSerializer


class CodeList(generics.ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
