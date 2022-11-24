from django.contrib import admin

from .models import Application, NginxConfCreateQueue

admin.site.register(Application)
admin.site.register(NginxConfCreateQueue)

# Register your models here.
