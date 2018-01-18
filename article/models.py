from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length = 20)
    auth = models.CharField(verbose_name='作者',max_length = 10)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add = True)
    modifytime = models.DateTimeField(verbose_name='修改时间',auto_now = True)
    content = models.TextField(verbose_name='内容')
    
    def __unicode__(self):
        return self.title
    
class Comments(models.Model):
    name = models.CharField(max_length = 20)
    messtime = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    article = ForeignKey(Article,on_delete=models.CASCADE)
    