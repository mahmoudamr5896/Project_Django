######################################libraries#########################################################
from asyncio import _register_task
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def my_protected_view(request):
    # Your view logic goes here
    return render(request, 'my_protected_template.html')
from django.contrib.auth.models import User

from django.contrib import messages
from django.urls import reverse
from .models import Tag
from audioop import ratecv
from unittest import loader
from urllib import request
from django.db.models import Avg, Sum
from django.shortcuts import get_object_or_404, render ,redirect
from django.http import HttpResponse
from .models import FeaturedProject, Picture, Project, Comment, Donation, Report, Rating ,Category
from .forms import  CommentReportForm, ProjectForm, CommentForm, DonationForm, ProjectReportForm, ReportForm, RatingForm
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.db.models import Q

from users.models import User
from .models import FeaturedProject, Project, Comment, Donation, Report, Rating,Tag ,Category
from .forms import ProjectForm, CommentForm, DonationForm, ReportForm, RatingForm
from django.db.models import Avg
from django.db.models import Q
from allauth.account.forms import LoginForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
#  Mahmoud Amr Working In home :
# def index(request):
    # return HttpResponse("Happy Day Mahmoud")
    # return render(request, 'myapp/home.html')
#_________________________________________________ _________________________________________________________________
import re
from django.db.models import Count
##########################################################################################################
NULL={}


def team(request):
    return render(request, 'myapp/ourTeam.html')

def getUser(request):
        user = _register_task.objects.get(id=request.session['user_id'])
        return user

def index(request):
    if 'user_id' in request.session:
        user = _register_task.objects.get(id=request.session['user_id'])
    else:
        user = None 
    
    categories = Category.objects.all()
    highest_rated_projects = Project.objects.annotate(rate=Avg('rating__value')).order_by('-rate')[:5]
    latest_projects = Project.objects.order_by('-start_time')[:5]
    latest_featured_projects = FeaturedProject.objects.order_by('-id')[:5]

    return render(request, 'myapp/home.html', {
        'categories': categories,
        'highest_rated_projects': highest_rated_projects,
        'latest_projects': latest_projects,
        'latest_featured_projects': latest_featured_projects,
        'user': user,
    })



def search(request):
    context = {}
    search_query = request.GET.get('search')
    print(search_query)
    if search_query:
        projects= Project.objects.filter(title=search_query)
        for search_query in projects:
            print(search_query.title)

        searched_tags =Tag.objects.filter()
        print(projects)
        print(searched_tags)
        context = {
            'search_query': search_query,
            'projects': projects,
            'searched_tags': searched_tags,
        }
    return render(request, "myapp/search-result.html", context)





def category_projects(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    projects = Project.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'myapp/showdataofcategory.html', {'projects': projects, 'categories': categories ,'category':category})

#_________________________________________________________________________________________________#

    
from .forms import ProjectForm, ImageForm  # Import the ImageFormSet

def create_project(request):
    ImageFormSet = inlineformset_factory(Project, Picture, form=ImageForm, extra=3)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            formset.instance = project
            formset.save()

            # Process tags
            tags_input = form.cleaned_data['tags']
            if tags_input:
                tags_list = [tag.strip() for tag in tags_input.split(',')]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    try:
                        project.tags.add(tag)
                    except Exception as e:
                        print(e)
            return redirect('project_list')
    else:
        form = ProjectForm()
        formset = ImageFormSet()
    return render(request, 'myapp/create_project.html', {'form': form, 'formset': formset})
 # Pass formset to template

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'myapp/project_list.html', {'projects': projects})

def tagged(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    projects = Project.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'projects': projects,
    }
    return render(request, 'myapp/home.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    comments = Comment.objects.filter(project=project)
    donations = Donation.objects.filter(project=project)
    reports = Report.objects.filter(project=project)
    ratings = Rating.objects.filter(project=project)
    tags = project.tags.all()
    similar_projects = Project.objects.filter(tags__in=tags).exclude(id=project.id).distinct()[:5]
    rating_form = RatingForm()
    average_rating = ratings.aggregate(Avg('value'))['value__avg']

    # Calculate the number of reports for the project
    report_count = reports.count()

    if report_count >= 15 and report_count < 20:
        # Display a warning message if the report count is close to 20
        messages.warning(request, f"Your project has received {report_count} reports. If it reaches 20, it will be deleted.")

    if report_count >= 20:
        # Delete the project and show a success message
        project.delete()
        messages.success(request, "Your project has been deleted due to receiving more than 20 reports.")

        # Redirect the user to a relevant page, such as the project list
        return redirect('project-list')

    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.project = project
            rating.user = request.user
            rating.save()
            return redirect('project-detail', project_id=project_id)
        if donation_form.is_valid():
            donation = donation_form.save(commit=False)
            donation.project = project
            donation.user = request.user
            donation.save()
            return redirect('project-detail', project_id=project_id)
    else:
        donation_form = DonationForm()
        rating_form = RatingForm()

    return render(request, 'myapp/project_detail.html', {
        'project': project,
        'comments': comments,
        'donations': donations,
        'reports': reports,
        'ratings': ratings,
        'rating_form': rating_form,
        'donation_form': donation_form,
        'average_rating': average_rating,
        'tags': tags,
        'similar_projects': similar_projects,
        'report_count': report_count,
    })
def add_comment(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project-detail', project_id=project_id)
    else:
        form = CommentForm()
    return render(request, 'myapp/add_comment.html', {'form': form})

def report_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.project = project
            report.user = request.user
            report.save()
            return redirect('project-detail', project_id=project_id)
    else:
        form = ReportForm()
    
    return render(request, 'myapp/report_project.html', {'form': form})

def report_comment(request, comment_id, project_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.comment = comment
            report.user = request.user
            report.save()
            # Redirect to the project list page after reporting successfully
            return redirect('project-detail', project_id=project_id)
    else:
        form = CommentReportForm()
    return render(request, 'myapp/report_comment_form.html', {'form': form})
# Similarly, implement views for donation, reporting, rating, and other actions




























@login_required
def profile(request):
    user_email = request.session.get("email")
    user_info = User.objects.get(email=user_email)
    context = {'user_info': user_info}
    return render(request, 'myapp/profile.html', context)

# modifed 
def login(request):
    return redirect(reverse('account_login'))



def sighup(request):
    return render(request, 'myapp/sighnup.html')




    # highest_rated_projects = Project.objects.annotate(
    #    avg_rate=Avg('rate__rate')).order_by('-avg_rate')[:5]
    # last_5_projects = Project.objects.all().order_by('-id')[:5]
    # featured_projects = Project.objects.filter(is_featured=1)[:5]

    # images = []
    # for project in highest_rated_projects:
    #     images.append(project.image_set.all().first().images.url)

    # context = {
    #     'highest_rated_projects':highest_rated_projects,
    #     'latest_5_projects': last_5_projects,
    #     'featured_projects': featured_projects,
    #     'images': images,
    #     'projects_count': len(Project.objects.all()),
    #     'donors_count': len(Donation.objects.all()),
    #     'reviews_count': len(ratecv.objects.all()),
    #     'user': user
    # }
    
    # html_template = loader.get_template('myapp/index.html')
    # return HttpResponse(html_template.render(context, request))