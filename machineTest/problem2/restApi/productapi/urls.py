from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns = [
    path('products/search/', views.SearchProductView.as_view(), name='search-product'),
    path("products/", views.AddProductView.as_view(), name='product'),
    path("products/<str:pk>/", views.EditProductView.as_view(), name='product'),
]