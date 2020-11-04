from django.urls import path
from .views import creategroupPageView

urlpatterns = [
    path('', creategroupPageView, name='creategroup')
]
