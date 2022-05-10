from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Course-home'),    #homepage
    path('<int:index>',views.home, name='Course-home')  #page for a specific course
]
