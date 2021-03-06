"""libmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from library import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('book_form',views.book_form,name='book_form'),
    path('allbooks',views.allbooks,name='allbooks'),
    path('<id>/',views.book_update,name="book_update"),
    path('delete/<id>/',views.book_delete,name="book_delete")


]
