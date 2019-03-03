from django.test import SimpleTestCase
from django.urls import resolve, reverse

from diagnosis_codes.views import CodeList, CodeDetail


class TestUrls(SimpleTestCase):

    def test_code_list_create_url_resolves(self):
        url  = reverse('code_list_create')
        self.assertEquals(resolve(url).func.view_class, CodeList)

    def test_code_detail_url_resolves(self):
        url = reverse('code_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, CodeDetail)
