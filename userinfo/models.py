from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("userinfo name",max_length=20)
    password = models.CharField("userinfo password",max_length=20)
    signdate = models.DateTimeField("sign date")
    interestnum = models.IntegerField("luckly number")
    isadmin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username