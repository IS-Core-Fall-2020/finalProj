from django.urls import path
from .views import viewclassesPageView, addclassPageView

urlpatterns = [
    path('', viewclassesPageView, name='viewclasses'),
    path('addclass/', addclassPageView, name='addclass'),
]
