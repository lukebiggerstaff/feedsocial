from django.contrib import admin
from django.urls import path, include
from .views import FeedView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
]