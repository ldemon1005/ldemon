from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^loginchat/$', views.LoginChat, name='loginchat'),
    url(r'^loginchatroom/$', views.LoginChatRoom, name='loginchat'),
    url(r'^logoutchat/$', views.LogoutChat, name='logoutchat'),
    url(r'^homechat/$', views.HomeChat, name='homechat'),
    url(r'^roomchat/$', views.RoomChat, name='roomchat'),

    url(r'^post/$', views.PostChat, name='post'),
    url(r'^messages/$', views.MessagesChat, name='messages'),
]