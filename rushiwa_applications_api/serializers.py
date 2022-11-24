from rest_framework import serializers

from .models import Application, NginxConfCreateQueue


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class NginxConfCreateQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NginxConfCreateQueue
        fields = '__all__'




