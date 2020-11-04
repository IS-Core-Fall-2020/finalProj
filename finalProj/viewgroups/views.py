from django.shortcuts import render
from django.http import HttpResponse

def viewgroupsPageView(request) :
    return HttpResponse('View Groups Here')