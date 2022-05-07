from django.db import models
from datetime import date, timedelta
from authentication.models import CustomUser


class Project(models.Model):
    choice = (
        ('Open', 'Open'),
        ('Close', 'Close')
    )
    user_id = models.ManyToManyField(CustomUser, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(choices=choice, max_length=10, default='Open')
    date_added = models.DateField(auto_now_add=True)
    date_closed = models.DateField(default=date.today()+timedelta(days=7))


class Task(models.Model):
    status_choices = (
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Done', 'Done'),
        ('Freezes', 'Freezes')
    )
    priority_choices = (
        ('High', 'High'),
        ('Mid', 'Mid'),
        ('Low', 'Low')
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(choices=status_choices, max_length=15, default='New')
    priority = models.CharField(choices=priority_choices, max_length=15, default='High')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=date.today()+timedelta(days=7))
    users_id = models.ManyToManyField(CustomUser, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)







