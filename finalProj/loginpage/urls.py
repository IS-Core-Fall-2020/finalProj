from django.urls import path
from .views import indexPageView, createaccountPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('createaccount/', createaccountPageView, name='createaccount')
]