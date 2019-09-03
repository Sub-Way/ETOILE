"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import *
from django.conf.urls import url
from django.contrib import admin
from polls import views
from CS import views
from HOME import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [


    # CS - Class-based views for CS

    url(r'^CS/', include(('CS.urls','CS'), namespace='CS')),

    url(r'^admin/', admin.site.urls),
    url(r'^HOME/', include(('HOME.urls','HOME'), namespace='HOME')),
    # url( r'^register/', include('REGISTER.urls', namespace='REGISTER')),
    url(r'^accounts/', include(('HOME.urls','accounts'), namespace='accounts')),
    url(r'^$', include(('HOME.urls','HOME'), namespace='HOME')),
    url(r'^photo/', include(('photo.urls','photo'), namespace='photo')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
