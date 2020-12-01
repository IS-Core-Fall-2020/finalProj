from django.urls import path
from .views import indexPageView, createaccountPageView, userPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('createaccount/', createaccountPageView, name='createaccount'),
    path('users/', userPageView, name='users'),
]