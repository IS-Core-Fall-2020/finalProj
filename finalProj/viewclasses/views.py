from django.shortcuts import render
from django.http import HttpResponse
from loginpage.models import Classes, Assignment

def viewclassesPageView(request) :

    class_queryList = Classes.objects.all()
    assignment_queryList = Assignment.objects.all()

    context = {
        'class_list' : class_queryList,
        'assignment_list' : assignment_queryList
    }

    return render(request, 'classes/viewclasses.html', context)

def addclassPageView(request) :
    return render(request, 'classes/addclass.html')