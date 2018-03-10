from django.db import models
from django.conf import settings

class UserContent(models.Model):
    content = models.TextField(max_length=280)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
