from django.urls import path
from django.contrib import admin
from .views import *



urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('create/', ContactCreateView.as_view(), name='contact-create'),
]
