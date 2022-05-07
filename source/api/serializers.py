import datetime
from django.utils import timezone
from rest_framework import serializers
from rest_framework.response import Response
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    check_date = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['user_id', 'name', 'description', 'status', 'date_added', 'date_closed', 'check_date']

        extra_kwargs = {'name': {'required': True},
                        'description': {'required': False},
                        'status': {'required': False},
                        'date_closed':{'required':False},
                        }


    def get_check_date(self, obj):
        check_date = ''
        date_closed = obj.date_closed
        date_now = datetime.datetime.date(timezone.now())
        if date_now > date_closed:
            check_date = 'Close'
            obj.status = check_date
            obj.save()
        return check_date

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority',
                  'created_date', 'updated_date', 'deadline', 'users_id', 'project_id']

        extra_kwargs = {'name': {'required': True},
                        'description': {'required': False},
                        'status': {'required': False},
                        'priority': {'required': False},
                        'created_date':{'required':False},
                        'updated_date':{'required':False},
                        'deadline':{'required':False},
                        'project_id':{'required':True}
                        }





