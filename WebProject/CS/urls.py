from django.conf.urls import url
from CS.views import *
from CS import views
from photo.models import Album, Photo, Categories
urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    url(r'^(?P<year>\d{4})/$', PostAV.as_view(), name='post_year_archive'),

    # Example: /add/

    url(r'^add/$', PostCreateView.as_view(), name="add",),

    # Example: /change/
    url(r'^change/$', PostChangeLV.as_view(), name="change",),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update",),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete",),

    url(r'^search/$', views.SearchFormView, name='search'),
    url(r'^searchPost/$', views.SearchPostView, name='searchPost'),
]