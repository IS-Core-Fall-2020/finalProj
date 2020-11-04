from django.shortcuts import render
from django.http import HttpResponse

def viewclassesPageView(request) :
    return HttpResponse('This is where you view and edit your group classwork')