from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'account/login.html')

def createaccountPageView(request) :
    return render(request, 'account/createaccount.html')