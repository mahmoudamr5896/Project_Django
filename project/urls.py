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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from myapp.views import add_comment, category_projects, create_project, index ,login, project_detail, project_list ,sighup,search, team,profile
from users import views as usersview



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index ,name='index'),
    path('<int:project_id>/', project_detail, name='project-detail'),
     path('project-list/', views.project_list, name='project-list'),
    path("login/",login ,name='login'),
    path("login/",login ,name='login'),
    path("/user/login/",sighup ,name='sighup'),
    path('search-result/', search, name='search-result'),
    path('create/',create_project, name='create'),
    path('list/', views.project_list, name='list'),
    path('<int:project_id>/comment/', add_comment, name='add-comment'),
    path('team/',team,name='team'),
    path('category/<int:category_id>/', category_projects, name='category_projects'),
<<<<<<< HEAD
    path('user/', include('allauth.urls')),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/', profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_user, name='delete_user'),
=======
     path('user/', include('allauth.urls')),
    path('profile/', usersview.view_profile, name='view_profile'),
    path('user/login/None', usersview.redirect_view),
    path('profile/edit/', usersview.edit_profile, name='edit_profile'),
    path('profile/delete/', usersview.delete_user, name='delete_user'),
    path('project_list/', project_list, name='project_list'),
    path('report-project/<int:project_id>/', views.report_project, name='report-project'),
    path('report-comment/<int:comment_id>/<int:project_id>/', views.report_comment, name='report-comment'),
>>>>>>> 6769bf20ecbc8a6daf94e209f736a909e8b6d504


    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
