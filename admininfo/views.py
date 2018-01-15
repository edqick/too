from django.shortcuts import render
from django.http import HttpResponse
from admininfo.models import Admininfo
# Create your views here.
def adminlogin(request):
    context = {}
    if request.method=='POST':
        #context['context'] = request.readlines()
        account = request.POST.get('admin',1)
        pwd = request.POST.get('admin-password',1)
        print('admin is : '+account+', pwd is : '+pwd)
        try:
            print('to try:')
            admin_info = Admininfo.objects.get(username=account,password=pwd)
            print('admin_info is : '+admin_info.password)
        except:
            return HttpResponse('account or password worry!')
        context['error'] = 'page not found'
    return render(request, 'error.html', context)
