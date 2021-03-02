from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add, name="add"),
    path('main/', views.index, name='main'),
    path('search/', views.search_asset, name='search'),
    path('assets/', views.my_assets, name='assets'),
    path('profile/', views.profile, name="profile"),

]
