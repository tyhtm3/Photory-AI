from django.db import models
from django.conf import settings
from storys.models import Story
# Create your models here.
class Article(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bookcover = models.ImageField(blank=True)
    story = models.ForeignKey(Story,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.IntegerField()

class Comment(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    story = models.ForeignKey(Story,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)