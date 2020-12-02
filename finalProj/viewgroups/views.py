from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import Classes, Group#, GroupMember

@login_required(login_url='/accounts/login')
def groupsPageView(request) :

    group_filterList = Group.objects.filter(user = request.user)
    
    context = {
        'group_list': group_filterList,
    
        }

    return render(request, 'groups/viewgroups.html', context)

def createGroupPageView(request) :
    return render(request, 'groups/creategroup.html')

def createGroup(request) :
    group = Group()
    group.group_name = request.POST.get('groupName')
    group.group_description = request.POST.get('groupDesc')
    group.user = request.POST.get('user')
    group.save()

    group_queryList = Group.objects.all()

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/creategroup.html', context)

