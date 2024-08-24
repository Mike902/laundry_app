from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('/contact', views.contact_page, name="contact_page")
]
