from django.contrib import admin
from django.urls import path, include
from .views import (FeedView, PFeedView,
                    ContentCreateView, CommentCreateView)

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create', ContentCreateView.as_view(), name='create' ),
    path('content/<int:pk>', CommentCreateView.as_view(), name='comment-create'),
    path('profile/<slug:user>', PFeedView.as_view(), name='pfeed'),
]
