from django.contrib import admin

from myapp.models import Category ,CommentReport, Donation, Picture, Project, Tag ,Comment, ProjectReport, Rating, Report , FeaturedProject


# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Report)
admin.site.register(ProjectReport)
admin.site.register(CommentReport)
admin.site.register(Donation)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(FeaturedProject)


