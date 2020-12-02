from django.urls import path
from .views import viewgroupsPageView, creategroupPageView, createGroup

urlpatterns = [
    path('',viewgroupsPageView, name='viewgroups'),
    path('creategroup/', creategroupPageView, name='creategroup'),
    path('newgroup/', createGroup, name='newgroup')
]
