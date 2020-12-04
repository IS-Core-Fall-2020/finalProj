from django.urls import path
from . import views

urlpatterns = [
    path('<int:groupID>/', views.assignPageView, name='viewassign'),
    path('edit/<int:assignID>/', views.editAssignPageView, name='editassign'),
    path('edit/', views.editAssignPageView, name='newassign'),
]   
