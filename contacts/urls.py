from django.contrib import admin
from django.urls import path
from . import views

app_name = "contacts"
urlpatterns = [
    path('/', views.page, name="contacts")
]
