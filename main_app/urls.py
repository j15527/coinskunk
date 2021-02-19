from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.index, name='main'),
    path('test/', views.test_page, name='test'),
]
