from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from loginpage.models import Classes, Group#, GroupMember

@login_required(login_url='/')
def viewgroupsPageView(request) :
    
    group_filterList = Group.objects.filter(user = request.user)
    
    context = {
        'group_list': group_filterList,
    
        }

    return render(request, 'groups/viewgroups.html', context)

def creategroupPageView(request) :
    return render(request, 'groups/creategroup.html')