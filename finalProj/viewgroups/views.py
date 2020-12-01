from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from loginpage.models import Group, User

#@login_required(login_url='login')
def viewgroupsPageView(request) :

    username = request.GET['username']
    password = request.GET['password']

    user = authenticate(username = username, password = password)

    if user is not None:
        group_queryList = Group.objects.all()

        context = {
            'group_list': group_queryList,

            }

        return render(request, 'groups/viewgroups.html', context)
    
    else: 
        return render(request, 'account/login.html')

def creategroupPageView(request) :
    return render(request, 'groups/creategroup.html')