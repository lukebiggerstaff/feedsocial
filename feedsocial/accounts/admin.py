from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FeedSocialUser

admin.site.register(FeedSocialUser, UserAdmin)
