from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

import json

from diagnosis_codes.models import DiagnosisCode
from diagnosis_codes.views import CodeList, CodeDetail


class TestViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.code_list_create_url = reverse('code_list_create')
        self.code_detail_url = reverse('code_detail', args=[1])


    def test_project_list_GET(self):
        response = self.client.get(self.code_list_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals([], response.data)
