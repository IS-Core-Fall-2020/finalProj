from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from loginpage.models import  Group, Assignment, UserPic
from viewgroups.forms import UserGroupForm, AssignmentForm
from django.contrib import messages

@login_required(login_url='/accounts/login')
def assignPageView(request, groupID) :
    #displays only the assignments of the specific group, and orders the assignments by 
    assign_filterList = Assignment.objects.filter(group_id = groupID).order_by('assign_duedate')
    group = Group.objects.get(id = groupID)

    context = {
        'assign_list': assign_filterList,
        'group': group
        }

    return render(request, 'classes/viewassignments.html', context)


#takes you to the edit Assignments page, filters by the selected Assignment.
def editAssignPageView(request, assignID = None) :
    #loggedInUser = User.objects.filter(username = request.user)
    parameter = None
    #groupID = Group.objects.get()
    if request.method == 'POST':
        #if there is a parameter being passed
        if assignID:
            parameter = Assignment.objects.get(id=assignID)
            if request.POST.get('delete'):
                parameter.delete()
                
            else:

                form = AssignmentForm(request.POST, instance = parameter)   
                form.save()
               
            return HttpResponseRedirect(f'/viewassignments/{parameter.group_id.id}')
        else:
            form = AssignmentForm(request.POST)
            #form filled in correctly
            if form.is_valid:
                form.save()

                return HttpResponseRedirect('/viewassignments/assignID')
    else:
        if assignID:
            parameter = Assignment.objects.get(id = assignID)
            #sends form and loads in the info from the parameter so you can see what you are editing
            form = AssignmentForm(instance = parameter)

        else: 
            #generates a blank form when you are creating a new Assignment
            form = AssignmentForm()
        
        #sends generated form and parameter (if there is one) to webpage
        context = {
            'form': form, 
            'parameter': parameter
        }

        return render(request, 'classes/editassignment.html', context)