from django.contrib import admin
from .models import Article

# Register your models here.
class articleAdmin(admin.ModelAdmin):
    fields = ('title','auth','content')
    
admin.site.register(Article,articleAdmin)