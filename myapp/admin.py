from django.contrib import admin

from myapp.models import Category, Comment, Donation, Picture, Project, Tag


# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Tag)
admin.site.register(Donation)
admin.site.register(Comment)
