import uuid

import django
from django.db import models


# Create your models here.
class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application_name = models.CharField(max_length=200, unique=True)
    framework = models.CharField(max_length=200)
    nginx_conf_path = models.BooleanField(default=False)
    local_git_repo = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    tag = models.CharField(max_length=200, default='latest')
    date_created = models.DateField(default=django.utils.timezone.now)
    def __str__(self):
        return self.application_name
    
class NginxConfCreateQueue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='pending')
    date_created = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.application.application_name