from django.shortcuts import render
from django.http import HttpResponse

def viewgroupsPageView(request) :
    return HttpResponse('View Groups Here')

def creategroupPageView(request) :
    return HttpResponse('This is where you create a new group')