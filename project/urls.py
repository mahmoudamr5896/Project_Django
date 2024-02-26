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
from myapp.views import add_comment, category_projects, create_project, index ,login, project_detail, project_list ,sighup,search, team




urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index ,name='index'),
    path("login/",login ,name='login'),
    path("sighup/",sighup ,name='sighup'),
    path('search-result/', search, name='search-result'),
    path('create/',create_project, name='create'),
    path('list/', project_list, name='list'),
    path('<int:project_id>/', project_detail, name='project-detail'),
    path('<int:project_id>/comment/', add_comment, name='add-comment'),
    path('team/',team,name='team'),
    path('category/<int:category_id>/', category_projects, name='category_projects'),

]
