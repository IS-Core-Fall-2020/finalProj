from django.urls import path

from . import views

urlpatterns = [
    path('', views.groupsPageView, name='viewgroups'),
    path('creategroup/', views.createGroupPageView, name='creategroup'),
    path('newgroup/', views.createGroup, name='newgroup'),
]
