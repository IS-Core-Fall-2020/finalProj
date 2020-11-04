from django.urls import path
from .views import viewclassesPageView

urlpatterns = [
    path('', viewclassesPageView, name='viewclasses')
]
