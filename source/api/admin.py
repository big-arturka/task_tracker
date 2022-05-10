from django.contrib import admin

from .models import Project,Task, Comment, Action
# Register your models here.

admin.site.register([Project, Task, Comment, Action])
