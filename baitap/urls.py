"""baitap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin

from django.conf.urls.static import static
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', views.index, name='index'),

    url(r'^home/student.html$', views.student, name='student'),
    url(r'^home/home/student.html$', views.student, name='student'),
    url(r'^home/home/index1.html$', views.index1, name='index1'),
    url(r'^home/index1.html$', views.index1, name='index1'),
    url(r'^home/student1.html$', views.student1, name='student1'),
    url(r'^home/home/student1.html$', views.student1, name='student1'),
    url(r'^', include('alpha.urls')),
    url(r'^index/$', views.index, name='index'),

    url(r'^index/home/student.html$', views.student, name='student'),
    url(r'^index/home/home/student.html$', views.student, name='student'),
    url(r'^index/home/home/index1.html$', views.index1, name='index1'),
    url(r'^index/home/index1.html$', views.index1, name='index1'),
    url(r'^index/home/student1.html$', views.student1, name='student1'),
    url(r'^index/home/home/student1.html$', views.student1, name='student1'),
]
if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
