from django.contrib import admin

from myapp.models import Category, CommentReport, Donation, Picture, Project, Comment, ProjectReport, Rating, Report 


# Register your models here.
# admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Report)
admin.site.register(ProjectReport)
admin.site.register(CommentReport)
admin.site.register(Donation)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Category)

from django.contrib import admin

from myapp.models import Category, Comment, Donation, Picture, Project


# Register your models here.
# admin.site.register(Category)
# # admin.site.register(Project)
# # admin.site.register(Picture)
# # admin.site.register(Tag)
# admin.site.register(Donation)
# admin.site.register(Comment)
