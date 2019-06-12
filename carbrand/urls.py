from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.brand_list, name='brandList'),
    path('json', views.brand_json_list, name='brandJsonList')
]
