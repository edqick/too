from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("用户名",max_length=20)
    password = models.CharField("密码",max_length=20)
    signdate = models.DateTimeField("注册日期")
    interestnum = models.IntegerField("幸运数字")
    isadmin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username