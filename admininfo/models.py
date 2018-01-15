from django.db import models

# Create your models here.
class Admininfo(models.Model):
    username = models.CharField("admin name",max_length=20)
    password = models.CharField("admin password",max_length=20)
    signdate = models.DateField("sign date")
    interestnum = models.IntegerField("luckly number")
    
    def __str__(self):
        return self.username + str(self.password) + self.signdate + str(self.interestnum)