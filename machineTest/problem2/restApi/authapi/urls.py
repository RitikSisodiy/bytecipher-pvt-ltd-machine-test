from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path("api/signup/", views.UserCreate.as_view(), name='signup')
]