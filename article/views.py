from django.shortcuts import render
from django.http import request
from .models import Article
from warnings import catch_warnings

# Create your views here.
def loadArticle(request):
    articles = Article.objects.all()
    #print(articles.values())
    return render(request, 'index-3.html', {'articles':articles.values()})

def contextArticle(request,pid):
    try:
        article = Article.objects.get(id=pid)
        articles = Article.objects.all()
        print(article)
        return render(request, 'blog/blog.html', {'article':article,'articles':articles})
    except:
        return render(request, 'error.html', {'error':'article not found!'})
    