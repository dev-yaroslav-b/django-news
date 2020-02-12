from django.conf import settings
from django.db import models
from markdownx.models import MarkdownxField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='user')
    text = MarkdownxField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text
