from django.shortcuts import render
from django.http import request
from .models import Article

# Create your views here.
def loadArticle(request):
    articles = Article.objects.all()
    print(articles.values('content'))
    return render(request, 'index-3.html', {'articles':articles.values()})