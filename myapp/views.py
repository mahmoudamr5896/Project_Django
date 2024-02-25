from asyncio import _register_task
from audioop import ratecv
from django.db.models import Avg, Sum
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Project, Comment, Donation, Report, Rating,Tag
from .forms import ProjectForm, CommentForm, DonationForm, ReportForm, RatingForm
from django.db.models import Avg

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

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            # Process tags
            tags_input = form.cleaned_data['tags']
            if tags_input:
                tags_list = [tag.strip() for tag in tags_input.split(',')]
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    project.tags.add(tag)
            return redirect('project-list')
    else:
        form = ProjectForm()
    return render(request, 'myapp/create_project.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'myapp/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    comments = Comment.objects.filter(project=project)
    donations = Donation.objects.filter(project=project)
    reports = Report.objects.filter(project=project)
    ratings = Rating.objects.filter(project=project)
    rating_form = RatingForm()

    # Calculate average rating
    average_rating = ratings.aggregate(Avg('value'))['value__avg']

    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        if donation_form.is_valid():
            donation = donation_form.save(commit=False)
            donation.project = project
            donation.user = request.user
            donation.save()
            return redirect('project-detail', project_id=project_id)
    else:
        donation_form = DonationForm()

    return render(request, 'myapp/project_detail.html', {'project': project, 'comments': comments, 'donations': donations, 'reports': reports, 'ratings': ratings, 'rating_form': rating_form, 'donation_form': donation_form, 'average_rating': average_rating})


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

# Similarly, implement views for donation, reporting, rating, and other actions






























#  get user from session
def login(request):
    return render(request, 'myapp/sighnup.html')

def sighup(request):
    return render(request, 'myapp/sighnup.html')



