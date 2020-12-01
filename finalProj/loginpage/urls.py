from django.urls import path
from .views import indexPageView#, createaccountPageView
from . import views

urlpatterns = [
    
    #path('createaccount/', createaccountPageView, name='createaccount'),
    path('register/', views.registerPage, name='register'),
    #path('login/', views.loginPage, name="login"),
    #path('logout/', views.logoutUser, name="logout"),

    path('', indexPageView, name='index'),
]