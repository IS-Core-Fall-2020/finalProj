from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import  Group, Assignment, UserPic

@login_required(login_url='/accounts/login')
def groupsPageView(request) :

    group_filterList = Group.objects.filter(user = request.user)
    
    context = {
        'group_list': group_filterList,
    
        }

    return render(request, 'groups/viewgroups.html', context)

def createGroupPageView(request) :

    user_queryList = User.objects.all()

    context = {
        'user_list': user_queryList,

        }

    return render(request, 'groups/creategroup.html', context)




def createGroup(request) :
    group = Group()
    group.group_name = request.POST.get('groupName')
    group.group_description = request.POST.get('groupDesc')
    group.save()

    #adds creator to the group
    add_to_group = User.objects.filter(username = request.user)
    group.user.add(add_to_group[0].id)

    #adds user 1
    group_member1 = request.POST.get('user1')
    add_to_group = User.objects.filter(username = group_member1)

    if request.POST.get('user1') == ' ':
        pass
    else : 
        group.user.add(add_to_group[0].id)

    #adds user 2
    group_member2 = request.POST.get('user2')
    add_to_group = User.objects.filter(username = group_member2)

    if request.POST.get('user2') == ' ':
        pass
    else : 
        group.user.add(add_to_group[0].id) 

    #adds user 3
    group_member3 = request.POST.get('user3')
    add_to_group = User.objects.filter(username = group_member3)

    if request.POST.get('user3') == ' ':
        pass
    else : 
        group.user.add(add_to_group[0].id) 

    #adds user 4
    group_member4 = request.POST.get('user4')
    add_to_group = User.objects.filter(username = group_member4)

    if request.POST.get('user4') == ' ':
        pass
    else : 
        group.user.add(add_to_group[0].id)

    group_queryList = Group.objects.all()

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/creategroup.html', context)





'''
def createGroup(request) :
    group = Group()
    group.group_name = request.POST.get('groupName')
    group.group_description = request.POST.get('groupDesc')
    group.save()

    add_to_group = User.objects.filter(username = request.user)
    group.user.add(add_to_group[0].id) 

    group_queryList = Group.objects.all()

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/creategroup.html', context)
'''








'''
def createGroup(request) :

    if request.method == 'POST':
        #Create a new employee object from the Employee model
        new_group = Group()
        #grab the data from the form and store it to the new object
        new_group.group_name = request.POST.get('groupName')
        new_group.group_description = request.POST.get('groupDesc')
        new_group.user = request.POST.get('user')
   

       
        #Save the contact information record to generate the id value for the contact
        new_group.save()
        #Store this newly created object/record identifier to the employee's contact info 1 to 1 relationship
        new_employee.contact_information = new_contact
        #Store the newly create state record to the employee atribute for the 1 to M relationship
        new_employee.emp_state = new_state
        #store the record form the model to the table
        new_employee.save()
      



    Group().group_name = request.POST.get('groupName')
    Group().group_description = request.POST.get('groupDesc')
    
    Group().user.set('user')
    
    Group().save()

    group_queryList = Group.objects.all()

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/creategroup.html', context)

'''