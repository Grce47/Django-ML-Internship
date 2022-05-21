from django.urls import path
from .views import runcode,home
urlpatterns = [
    path('',home, name='Course-home'),    #homepage
    path('<int:index>',home, name='Course-home'),  #page for a specific course
]
