from django.db import models
from django.contrib.auth.models import AbstractUser

class FeedSocialUser(AbstractUser):
    class Meta:
        unique_together = ('username',)
