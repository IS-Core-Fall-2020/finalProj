from django.shortcuts import render
from django.http import HttpResponse

def viewgroupsPageView(request) :
    return render(request, 'groups/viewgroups.html')

def creategroupPageView(request) :
    return render(request, 'groups/creategroup.html')