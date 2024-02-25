from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project, Comment, Donation, Report, Rating, Tag
from .forms import ProjectForm, CommentForm, DonationForm, ReportForm, RatingForm
from django.db.models import Avg

# Create your views here.
def index(request):
    # return HttpResponse("Happy Day Mahmoud")
    return render(request, 'myapp/home.html')


def login(request):
    return render(request, 'myapp/sighnup.html')

def sighup(request):
    return render(request, 'myapp/sighnup.html')



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
            return redirect('project_list')
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
            return redirect('myapp/project_detail', project_id=project_id)
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
            return redirect('project_detail', project_id=project_id)
    else:
        form = CommentForm()
    return render(request, 'myapp/add_comment.html', {'form': form})




