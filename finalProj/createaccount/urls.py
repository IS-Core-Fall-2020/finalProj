from django.urls import path
from .views import createaccountPageView

urlpatterns = [
    path('', createaccountPageView, name='createaccount')
]
