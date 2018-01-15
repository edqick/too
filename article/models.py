from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 20)
    auth = models.CharField(max_length = 10)
    createtime = models.DateTimeField(auto_now_add = True)
    modifytime = models.DateTimeField(auto_now = True)
    content = models.TextField()
    
class Comments(models.Model):
    name = models.CharField(max_length = 20)
    messtime = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    article = ForeignKey(Article,on_delete=models.CASCADE)
    