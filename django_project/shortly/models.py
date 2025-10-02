from django.db import models
from django.contrib.auth.models import User


class ShortenedUrl(models.Model):
    base_url = models.URLField()
    short_url = models.URLField(db_index=True)
    alias = models.TextField(max_length=50)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
