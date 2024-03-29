"""ml_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from User import views as User_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),    #admin pages
    path('course/',include('Course.urls')), #course homepage
    path('signup/',User_views.signup,name='User-signup'),   #sign up page
    path('',auth_views.LoginView.as_view(template_name='User/login.html'),name='User-login'),   #log in page
    path('logout/',auth_views.LogoutView.as_view(template_name='User/logout.html'),name='User-logout'), #log out page
    path('callback/',User_views.callback,name='callback'),
    path('download/',User_views.download_data,name='User-download'),
    path('password/',User_views.change_password,name='change_password'),
]
