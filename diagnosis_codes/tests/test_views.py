from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

import json

from diagnosis_codes.models import DiagnosisCode, Category
from diagnosis_codes.views import CodeList, CodeDetail


class TestCodeListViews(APITestCase):
    """
        Tests for CodeList View.
    """
    def setUp(self):
        self.client = APIClient()
        self.code_list_create_url = reverse('code_list_create')
        self.code_detail_url = reverse('code_detail', args=[1])
        self.category =  Category.objects.create(version="ICD-10-2018",
                                                 code="A00",
                                                 title="Cholera")

    def test_code_list_GET(self):
        response = self.client.get(self.code_list_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals([], response.data['results'])

    def test_code_creation_POST(self):
        data = {
            "version": "ICD-10-2018",
            "category_code": "A00",
            "diagnosis_code": 233,
            "full_code": "A11233",
            "abbreviated_description": "fasdf",
            "full_description": "This is malaria",
            "category_title": "Cholera"
        }
        response = self.client.post(self.code_list_create_url,
                                    data,
                                    format='json')
        self.assertEquals(response.status_code, 201)
        
    def test_code_creation_returns_400_error_with_bad_data(self):
        bad_data = {
            "category_cde": "A013",
            "diagnosis_cde": 233,
            "full_code": "A11233",
            "abbreviated_description": "fasdf",
            "full_description": "This is malaria",
            "category_title": "Cholera from postman"
        }
        response = self.client.post(self.code_list_create_url,
                                    bad_data,
                                    format='json')
        self.assertEquals(response.status_code, 400)



class TestCodeDetailViews(APITestCase):
    """
        Test for CodeDetail View
    """
    def setUp(self):
        self.client = APIClient()
        self.create_url_name = "code_list_create"
        self.detail_url_name = "code_detail"
        self.post_data = {
            "version": "ICD-10-2018",
            "category_code": "A00",
            "diagnosis_code": 233,
            "full_code": "A11233",
            "abbreviated_description": "fasdf",
            "full_description": "This is malaria",
            "category_title": "Cholera"
        }
        self.category =  Category.objects.create(version="ICD-10-2018",
                                            code="A00",
                                            title="Cholera")

    def test_retrieving_code_by_id(self):
        post_response = self.client.post(reverse(self.create_url_name),
                         self.post_data,
                         format='json')
        response = self.client.get(reverse(self.detail_url_name,
                                   args=[post_response.data["id"]]))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], post_response.data["id"])

    def test_code_detial_returns_404_for_bad_ids(self):
        response = self.client.get(reverse(self.detail_url_name, args=[22]))
        self.assertEquals(response.status_code, 404)

    def test_deleting_code_item_by_id(self):
        post_response = self.client.post(reverse(self.create_url_name),
                                                 self.post_data,
                                                 format='json')
        response = self.client.delete(reverse(self.detail_url_name,
                                      args=[post_response.data["id"]]))
        self.assertEquals(response.status_code, 204)

    def test_updating_existing_code_item(self):
        post_response = self.client.post(reverse(self.create_url_name),
                                 self.post_data,
                                 format='json')
        response = self.client.put(reverse(self.detail_url_name, 
                                           args=[post_response.data['id']]),
                                   {"abbreviated_description": "fasdf",
                                    "full_description": "This is malaria",
                                    "full_code": "new_code",
                                    "category": self.category.id},
                                    format='json')
        self.assertEquals(response.data['full_code'], "new_code")
        
    
