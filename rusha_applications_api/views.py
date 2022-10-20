import json

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import generics

from .models import Application, NginxConfCreateQueue
from .serializers import ApplicationSerializer, NginxConfCreateQueueSerializer

# Create your views here.

@csrf_exempt
def application_list(request):
    """
    retrieve:
    """

    if request.method == 'GET':
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@transaction.atomic
@require_http_methods(["POST"])
def deploy_application(request):
    """
    retrieve:
    """   
    try:
       
        data = json.loads(request.body)
        framework = data.get('framework')
        application_name = data.get('applicationName')
        application_dict = {
            'framework': framework,
            'application_name': application_name
        }
        app_serializer = ApplicationSerializer(data=application_dict)
        print(app_serializer.is_valid())        
        if app_serializer.is_valid():
            a = Application.objects.create(**app_serializer.validated_data)
           
        else:
            print(application_dict)
            print(app_serializer.errors)
            return JsonResponse(app_serializer.errors, status=400)

        #  insert into NginxConfCreateQueue
        print(app_serializer.data)
        print(a.pk)

        nginx_queue_dict = {
            'application': a.pk
        }
        nginx_serializer = NginxConfCreateQueueSerializer(data=nginx_queue_dict)
        if nginx_serializer.is_valid():
            NginxConfCreateQueue.objects.create(**nginx_serializer.validated_data)
        else:
            print(nginx_serializer.errors)
            return JsonResponse(nginx_serializer.errors, status=400)
        return JsonResponse(app_serializer.data, status=201)
    
    except Exception as e:
        print(f'exception {e}')
        return JsonResponse({'status': 'failed'}, safe=False)
        

   

    # if request.method == 'POST':
   