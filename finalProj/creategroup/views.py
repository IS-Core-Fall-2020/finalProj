from django.shortcuts import render
from django.http import HttpResponse

def creategroupPageView(request) :
    return HttpResponse('This is where you create a new group')