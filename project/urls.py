"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
<<<<<<< HEAD
from myapp.views import add_comment, create_project, index ,login, project_detail, project_list ,sighup

=======
from myapp.views import index ,login ,sighup 
>>>>>>> a3c7d0dee969aa83de1acca9609b6a75baa9c192



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index ,name='index'),
    path("login/",login ,name='login'),
    path("sighup/",sighup ,name='sighup'),
<<<<<<< HEAD
    
    path('create/',create_project, name='create-project'),
    path('list/', project_list, name='project-list'),
    path('<int:project_id>/', project_detail, name='project-detail'),
    path('<int:project_id>/comment/', add_comment, name='add-comment'),
=======
    # path('create/', create_project, name='create-project'),
    # path('list/', project_list, name='project-list'),
    # path('<int:project_id>/', project_detail, name='project-detail'),
    # path('<int:project_id>/comment/', add_comment, name='add-comment'),
>>>>>>> a3c7d0dee969aa83de1acca9609b6a75baa9c192
]
