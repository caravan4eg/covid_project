from django.contrib import admin
from .models import Fact, Location, Photo, Post, Project

admin.site.register(Fact)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(Post)
admin.site.register(Project)
