from django.conf.urls import url
from HOME.views import *
from HOME import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from django.views.generic import TemplateView
from HOME.views import signup, UserCreateDoneTV,UserCreateView, login, logout, legal
from HOME.models import temp
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^woman/$', views.woman, name='woman'),
    url(r'^man/$', views.man, name='man'),
    path('auth/',include('django.contrib.auth.urls')),
    #url(r'^', include('django.contrib.auth.urls','good'),namepsace=good),
    url(r'^register/$', UserCreateView.as_view(), name='register'),
    url(r'^register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^login/$', views.login, name='login'),
    path('logout/',LoginView.as_view(), name='logout'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^legal/$', legal.as_view(), name='legal'),
    url(r'^about/$', TemplateView.as_view(
        template_name='HOME/about.html'
    ), name='about'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),

    url(r'^orderlist/$', views.orderlist,name='order_list'),
    url(r'^mypage/$', views.update_profile, name='mypage'),

]
