from django.urls import path

from .views import application_list, deploy_application

urlpatterns = [
    path('applications/', application_list),
    path('deploy/', deploy_application),
]