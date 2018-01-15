from django.shortcuts import render
from django.http import HttpResponse, response
from userinfo.models import User
from _datetime import datetime
from _random import Random
# Create your views here.
def users(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username',1)
        password = request.POST.get('password',1)
        print('userinfo is : '+username+', pwd is : '+password)
        try:
            user_info = User.objects.get(username=username,password=password)
            return render(request, 'hello.html')
        except:
            return HttpResponse('account or password worry!')
        context['error'] = 'page not found'
    return render(request, 'error.html', context)

def login(request):
    return render(request, 'login.html')

def logout(request):
    pass

def error(request):
    pass

def create(request):
    if request.method == 'POST':
        username = request.POST.get('username',1)
        password = request.POST.get('password',1)
        print('userinfo is : '+username+', pwd is : '+password)
        User.objects.create(username=username,password=password,signdate=datetime.now(),interestnum=1,isadmin=False)
        return HttpResponse('user create success!')

