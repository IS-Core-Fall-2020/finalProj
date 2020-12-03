from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import  Group, Assignment, UserPic
from viewgroups.forms import UserGroupForm
from django.contrib import messages

@login_required(login_url='/accounts/login')
def groupsPageView(request) :

    group_filterList = Group.objects.filter(user = request.user)
    
    context = {
        'group_list': group_filterList,
    
        }

    return render(request, 'groups/viewgroups.html', context)

'''
#called when enterting the create group page, loads up all users that you may connect them to the new group object you create
def createGroupPageView(request) :



    user_queryList = User.objects.all()

    context = {
        'user_list': user_queryList,

        }

    return render(request, 'groups/creategroup.html', context)



#called when finalizing the new group, loads up the info input on the new group page, creates the group, and redirects you to the current groups page
#blank strings were input into the select boxes for asthetic reasons, and so that you dont have to add a person you dont want to
#If the same user is added twice via the select boxes, the system will only add them once.
def createGroup(request) :
    group = Group()
    group.group_name = request.POST.get('groupName')
    group.group_description = request.POST.get('groupDesc')
    group.save()

    #adds logged in user to the group automatically
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

    if request.POST.get('user2') != ' ':
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
    #redirects back to the viewgroups.html page to see all your groups
    return render(request, 'groups/viewgroups.html', context)
'''

#takes you to the edit groups page, filters by the selected group.
def editGroupPageView(request, groupID = None) :
    
    parameter = None
    if request.method == 'POST':
        if groupID:
            parameter = Group.objects.get(id=groupID)
            if request.POST.get('delete'):
                parameter.delete()
                
            else:
                
                form = UserGroupForm(request.POST, instance = parameter)
                form.save()
                
               
            return HttpResponseRedirect('/viewgroups')
        else:
            form = UserGroupForm(request.POST)
            if form.is_valid:
                form.save()

              

                return HttpResponseRedirect('/viewgroups')
    else:
        if groupID:
            parameter = Group.objects.get(id = groupID)
            form = UserGroupForm(instance = parameter)

        else: 
            form = UserGroupForm()
        
        context = {
            'form': form, 
            'parameter': parameter
        }

        return render(request, 'groups/editgroup.html', context)



def newGroupView(request, groupID = None):

    parameter = None
    if request.method == 'POST':
        if groupID:
            parameter = Group.objects.get(id=groupID)
            if request.POST.get('delete'):
                parameter.delete()
                
            else:
                
                form = UserGroupForm(request.POST, instance = parameter)
                form.save()
                
               
            return HttpResponseRedirect('/viewgroups')
    else:
        if groupID:
            parameter = Group.objects.get(id = groupID)
            form = UserGroupForm(instance = parameter)

        else: 
            form = UserGroupForm()
        
        context = {
            'form': form, 
            'parameter': parameter
        }

        return render(request, 'groups/editgroup.html', context)



'''
def editGroupFinalize(request, groupID) :
   
    #group = Group.objects.filter(id = groupID)

    group = Group.objects.get(id = groupID)
    users = User.objects.all()
    #group = group_filterList.objects.get(emp_first=sFirst, emp_last=sLast) 

    group.group_name = request.POST.get('groupName')
    group.group_description = request.POST.get('groupDesc')
    group.save()

    #adds logged in user to the group automatically
    #add_to_group = User.objects.filter(username = request.user)
    #group.objects.get(user)


    group.save()

    group_queryList = Group.objects.all()

    

    context = {
        'group_list': group_queryList,

        }

    return render(request, 'groups/viewgroups.html', context)
'''

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