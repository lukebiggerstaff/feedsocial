from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignupView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page' : '/' }, name='logout'),
]

