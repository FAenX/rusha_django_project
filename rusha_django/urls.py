"""rusha_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def create_super_user(request):
    try:
        from django.contrib.auth.models import User
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        return HttpResponse('Super user created')
    except:
        return HttpResponse('Super user not created')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-api/v1/', include('rushiwa_applications_api.urls')),
    path('create_super_user/', create_super_user),
]
