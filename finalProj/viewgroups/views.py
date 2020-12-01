from django.shortcuts import render
from django.http import HttpResponse
from .models import Group

def viewgroupsPageView(request) :
    Data = Group.objects.all()

    context = {
        'groups' : Data
    }
    return render(request, 'groups/viewgroups.html', context)

def creategroupPageView(request) :
    return render(request, 'groups/creategroup.html')
