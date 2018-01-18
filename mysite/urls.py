"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import view
from userinfo import urls as user
from article import urls as arter
from django.conf.urls import include
from django.contrib import admin
'''userinfo.site.urls'''
'''
admin    :superuser
password:super1234
'''
urlpatterns = [
    url(r'^$', view.index,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', view.index,name='home'),
    url(r'^album/$', view.album,name='album'),
    url(r'^network/$', view.network,name='network'),
    url(r'^blog/', include(arter, namespace='blog')),
    url(r'^contact/$', view.contact,name='contact'),
    url(r'^login/', include(user, namespace = 'userinfo')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
