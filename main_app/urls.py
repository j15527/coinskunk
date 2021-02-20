from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.index, name='main'),
    path('test/', views.test_page, name='test'),
    path('assets/', views.my_assets, name='assets'),
    path('profile/', views.profile, name="profile"),
]
