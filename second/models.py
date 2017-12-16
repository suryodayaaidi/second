from django.db import models

class Article(models.Model):
    no = models.IntegerField(primary_key=True);
    title = models.CharField(max_length=32);
    post = models.CharField(max_length=2048);

