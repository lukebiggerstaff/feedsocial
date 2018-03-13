from django.contrib import admin
from django.urls import path, include
from .views import (FeedView, PFeedView,
                    ContentCreateView)

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create', ContentCreateView.as_view(), name='create' ),
    path('profile/<slug:user>', PFeedView.as_view(), name='pfeed'),
]
