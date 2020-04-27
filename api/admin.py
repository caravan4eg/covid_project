from django.contrib import admin
from .models import Fact, Location, Image, Post, Project

admin.site.register(Fact)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Project)
