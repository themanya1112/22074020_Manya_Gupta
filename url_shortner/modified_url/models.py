from django.db import models

class URL(models.Model):
    long_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=15, unique=True)
