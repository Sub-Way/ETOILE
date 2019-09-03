from django.conf.urls import url
from photo.views import *
from django.views.generic import ListView, DetailView, TemplateView
from photo.models import Album, Photo, Categories ,Cart
from photo import views
urlpatterns = [
    # Example: /
    url(r'^$', ListView.as_view(model=Album), name='index'),

    # Example : /album/, same as /
    url(r'^album/$', ListView.as_view(model=Album), name='album_list'),


    # Example: /album/99/

    url(r'^album/(?P<album_id>\d+)/$', views.album_detail, name='album_detail'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', DetailView.as_view(model=Photo), name='photo_detail'),

    # Example: /album/add
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name="album_add",),

    # Example: /album/change/
    url(r'^album/change/$', AlbumChangeLV.as_view(), name="album_change",),

    # Example: /album/99/update

    url(r'^album/(?P<pk>[0-9]+)/update/$', AlbumPhotoUV.as_view(), name="album_update",),

    # Example: /album/99/delete

    url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDeleteView.as_view(), name="album_delete",),

    # Example: /photo/add/
    url(r'^photo/add/$', PhotoChangeLV.as_view(), name ="photo_cahnge",),

    # Example: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$', PhotoUpdateView.as_view(), name="photo_update",),

    # Example: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', PhotoDeleteView.as_view(), name="photo_delete",),


    url(r'^test/(?P<pk>\d+)/$', testView.as_view(), name='test'),
    url(r'^m_bag/$', MbagLV.as_view(), name="m_bag"),
    url(r'^m_cloth/$', MclothLV.as_view(), name="m_cloth"),
    url(r'^m_fashion/$', MfashionLV.as_view(), name="m_fashion"),
    url(r'^m_shoe/$', MshoeLV.as_view(), name="m_shoe"),
    url(r'^m_wallet/$', MwalletLV.as_view(), name="m_wallet"),
    url(r'^w_bag/$', WbagLV.as_view(), name="w_bag"),
    url(r'^w_cloth/$', WclothLV.as_view(), name="w_cloth"),
    url(r'^w_fashion/$', WfashionLV.as_view(), name="w_fashion"),
    url(r'^w_shoe/$', WshoeLV.as_view(), name="w_shoe"),
    url(r'^w_wallet/$', WwalletLV.as_view(), name="w_wallet"),
    url(r'^m_bag/(?P<pk>\d+)/$', DetailView.as_view(model=Categories), name='Categories_detail'),
    # url(r'^wow/$', views.choice, name='choice'),
    url(r'^cart/$', views.CartOrBuy
    , name='cart'),
    url(r'^carts/$', views.view, name="cartbag"),
    url(r'^cart/(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'), #장바구니 삭제
    url(r'^orderlist/$', views.orderlist, name="orderlist"),
    url(r'^orderlist2/$', views.sendorderlist, name="sendorderlist"),
    url(r'^orderlist3/$',views.cartorderlist,name="cartorderlist"),
    url(r'^orderlist4/$', views.sendorderlist2, name="sendorderlist2"),
]