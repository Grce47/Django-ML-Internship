from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Course-home'),
    path('<int:index>',views.home, name='Course-home')
]
