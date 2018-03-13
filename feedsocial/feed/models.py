from django.db import models
from django.conf import settings

class UserContent(models.Model):
    content = models.TextField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

class ContentComment(models.Model):
    message = models.TextField(max_length=140)
    content_parent = models.ForeignKey(
        'UserContent',
        on_delete = models.CASCADE,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
