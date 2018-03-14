from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignupView
from .forms import FeedSocialAuthForm

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login/', auth_views.login,{'authentication_form' : FeedSocialAuthForm}, name='login'),
    path('logout/', auth_views.logout, {'next_page' : '/' }, name='logout'),
]

