from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Login Page')