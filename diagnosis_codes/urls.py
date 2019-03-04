from django.conf.urls import url
from .views import CodeList, CodeDetail, CategoryList


urlpatterns = [
    url(r'codes/$', CodeList.as_view(), name='code_list_create'),
    url(r'codes/(?P<pk>\d+)$', CodeDetail.as_view(), name='code_detail'),
    url(r'categories/$', CategoryList.as_view(), name='category_list_create'),
]