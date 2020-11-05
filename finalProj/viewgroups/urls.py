from django.urls import path
from .views import viewgroupsPageView, creategroupPageView

urlpatterns = [
    path('',viewgroupsPageView, name='viewgroups'),
    path('creategroup/', creategroupPageView, name='creategroup'),
]
