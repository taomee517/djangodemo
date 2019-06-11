from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/', views.brand_list, name='brandList')
]
