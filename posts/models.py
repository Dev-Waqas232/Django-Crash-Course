from django.db import models

# Create your models here.

class Post(models.Model):
    # Whenever you assign fields, think about web forms and what type of fields you are going to use like input type text or textarea etc
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)