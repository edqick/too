from django.shortcuts import render
from django.http import request
from .models import Article,Comments
from userinfo.models import User
import traceback
from django.urls.base import reverse
# Create your views here.
def loadArticle(request):
    articles = Article.objects.all()
    #print(articles.values())
    return render(request, 'index-3.html', {'articles':articles.values()})

def contextArticle(request,pid):
    articles = Article.objects.all()
    article = Article.objects.filter(pk=pid)
    if len(article)==0:
        return render(request, 'error.html', {'error':'article not found!'})
    if request.method == 'POST':#增加评论
        review = request.POST.get('review')
        user = User.objects.get(username=article[0].auth)
        Comments.objects.create(name=user,content=review,article=article[0])
    
    comments = Comments.objects.filter(article=article[0])[::-1]
    context = {'article':article[0],'articles':articles,'comments':comments}
    return render(request, 'blog/blog.html', context)
        