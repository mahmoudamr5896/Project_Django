from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pictures = models.ManyToManyField('Picture', blank=True)
    total_target = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField('Tag', blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Picture(models.Model):
    image = models.ImageField(upload_to='project_images/')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    donated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)

