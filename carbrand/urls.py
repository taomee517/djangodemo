from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/list', views.brand_list, name='brandList'),
    path('brand/json', views.brand_json_list, name='brandJsonList')
]
