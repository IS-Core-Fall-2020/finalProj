from django.urls import path
from .views import addclassPageView

urlpatterns = [
    path('', addclassPageView, name='addclass')
]
