from django.shortcuts import render
from django.http import HttpResponse

def viewclassesPageView(request) :
    return render(request, 'classes/viewclasses.html')

def addclassPageView(request) :
    return render(request, 'classes/addclass.html')