from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from loginpage.models import Group

#@login_required(login_url='login')
def viewgroupsPageView(request) :
    group_queryList = Group.objects.all()

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/viewgroups.html', context)

def creategroupPageView(request) :
    return render(request, 'groups/creategroup.html')