from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from baitap import settings
from home.models import *

from .models import Chat


def LoginChat(request):
    logout(request)
    next = request.GET.get('next', '/homechat/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/loginchat.html", {'next': next})

def LoginChatRoom(request):
    logout(request)
    global lienkhoa
    next = request.GET.get('next', '/roomchat/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name=request.POST['first_name']
        lienkhoa = first_name
        user = authenticate(username=username, password=password)

        if user is not None:
            if (user.first_name == lienkhoa):
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect('/loginchatroom/')
    return render(request, "alpha/loginchatroom.html", {'next': next})
def LogoutChat(request):
    logout(request)
    return HttpResponseRedirect('/loginchat/')

def LogoutChatRoom(request):
    logout(request)
    return HttpResponseRedirect('/loginchatroom/')
def HomeChat(request):
    c = Chat.objects.all()
    return render(request, "alpha/homechat.html", {'home': 'active', 'chat': c})

def RoomChat(request):

    c = Chat.objects.filter(user__first_name=lienkhoa)
    return render(request, "alpha/roomchat.html", {'home': 'active', 'chat': c})

def PostChat(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message= msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': c.user.username +' : '+ msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def MessagesChat(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messageschat.html', {'chat': c})