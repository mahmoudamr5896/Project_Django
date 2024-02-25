# forms.py
from django import forms
from .models import CommentReport, Project, Comment, Donation, ProjectReport, Report, Rating

class ProjectForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False) 
    class Meta:
        model = Project
        fields = ['title', 'details', 'category', 'total_target', 'start_time', 'end_time']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
        
class ProjectReportForm(forms.ModelForm):
    class Meta:
        model = ProjectReport
        fields = ['reason']

class CommentReportForm(forms.ModelForm):
    class Meta:
        model = CommentReport
        fields = ['reason']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.Select(choices=Rating.RATING_CHOICES)
        }
