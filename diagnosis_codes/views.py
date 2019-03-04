from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

from diagnosis_codes.models import DiagnosisCode, Category
from diagnosis_codes.serializers import (DiagnosisCodeSerializer,
                                         CategorySerializer)


class CodeList(APIView):
    """
        List all diagnosis codes, or create a new code
    """

    def get(self, request, format=None):
        codes = DiagnosisCode.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 20
        page = paginator.paginate_queryset(codes, request)
        serializer = DiagnosisCodeSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        try:
            version_name = request.data['version']
            category_title = request.data['category_title']
            category_code = request.data['category_code']
        except KeyError as e:
            return Response({"error": "Check data. {} missing".format(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            category = Category.objects.get(version=version_name,
                                            code=category_code,
                                            title=category_title)
        except ObjectDoesNotExist:
            return Response({"error": "Invalid Category"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        del request.data['category_title'], request.data['category_code']
        request.data['category'] = category.id

        serializer = DiagnosisCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodeDetail(APIView):
    """
        Retrieve, Update or Delete an single code entry.
    """
    def get_object(self, pk):
        try:
            return DiagnosisCode.objects.get(pk=pk)
        except DiagnosisCode.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        code = self.get_object(pk)
        serializer = DiagnosisCodeSerializer(code)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        code = self.get_object(pk)
        request.data['category'] = code.category.id
        serializer = DiagnosisCodeSerializer(code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        code = self.get_object(pk)
        code.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)