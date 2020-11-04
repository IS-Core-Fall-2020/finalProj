from django.shortcuts import render
from django.http import HttpResponse

def addclassPageView(request) :
    return HttpResponse('This is where you add a class to the group')