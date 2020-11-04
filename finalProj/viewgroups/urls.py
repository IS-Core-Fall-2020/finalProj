from django.urls import path
from .views import viewgroupsPageView

urlpatterns = [
    path('',viewgroupsPageView, name='viewgroups')
]
