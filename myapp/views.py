from asyncio import _register_task
from audioop import ratecv
from django.db.models import Avg, Sum
from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader

from .models import Donation, Project

# Create your views here.

#  Mahmoud Amr Working In home :
def index(request):
    # return HttpResponse("Happy Day Mahmoud")

    return render(request, 'myapp/home.html')
NULL={}

def getUser(request):
        user = _register_task.objects.get(id=request.session['user_id'])
        return user

# def index(request):
#     if 'user_id' in request.session:
#         user = getUser(request)
#     else:
#         user = NULL 
#     highest_rated_projects = Project.objects.annotate(
#        avg_rate=Avg('rate__rate')).order_by('-avg_rate')[:5]
#     last_5_projects = Project.objects.all().order_by('-id')[:5]
#     featured_projects = Project.objects.filter(is_featured=1)[:5]

#     images = []
#     for project in highest_rated_projects:
#         images.append(project.image_set.all().first().images.url)

#     context = {
#         'highest_rated_projects':highest_rated_projects,
#         'latest_5_projects': last_5_projects,
#         'featured_projects': featured_projects,
#         'images': images,
#         'projects_count': len(Project.objects.all()),
#         'donors_count': len(Donation.objects.all()),
#         'reviews_count': len(ratecv.objects.all()),
#         'user': user
#     }
    
#     html_template = loader.get_template('myapp/index.html')
#     return HttpResponse(html_template.render(context, request))


#  get user from session


def login(request):
    return render(request, 'myapp/sighnup.html')

def sighup(request):
    return render(request, 'myapp/sighnup.html')

