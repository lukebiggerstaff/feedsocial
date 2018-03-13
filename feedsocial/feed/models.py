from django.db import models
from django.conf import settings
from django.utils import timezone


class UserContent(models.Model):
    content = models.TextField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    num_comments = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "{}: {}".format(self.content, self.creator.username)

    class Meta:
        ordering = ['-last_updated', ]

class ContentComment(models.Model):
    message = models.TextField(max_length=140)
    content_parent = models.ForeignKey(
        'UserContent',
        on_delete = models.CASCADE,
    )
    comment_creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    creation_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.content_parent.creator != self.comment_creator:
            self.content_parent.last_updated = timezone.now()
        self.content_parent.num_comments += 1
        self.content_parent.save()
        return super(ContentComment, self).save(*args, **kwargs)

    def __repr__(self):
        return "{}: {}".format(self.message, self.comment_creator.username)
