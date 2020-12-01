from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def indexPageView(request) :
    return render(request, 'account/login.html')

def createaccountPageView(request) :
    return render(request, 'account/createaccount.html')

def userPageView(request) :
    data = User.objects.all()

    context = {
        'user' : data
    }

    return render(request, 'account/displayUsers.html', context)