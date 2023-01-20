"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/',views.UserView.as_view(),name='signup'),
    path("",views.LoginView.as_view(),name="signin"),
    path('home/',views.HomeView.as_view(),name='home'),
    path('logout/',views.logout_view,name='logout'),
    path("home/<int:id>/check/",views.check_task_view,name='check_task'),
    path("home/<int:id>/uncheck/",views.uncheck_task_view,name='uncheck_task'),
    path('home/<int:id>/temp-remove/',views.temp_task_delete_view,name='temp-remove-task'),
    path('home/<int:id>/remove/',views.task_delete_view,name='remove-task'),
    path('home/removedtasks/',views.get_all_removed_tasks,name='removedtasks'),
    path('changepassword/',views.ChangePasswordView.as_view(),name='changepassword')
]
