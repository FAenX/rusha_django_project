# Generated by Django 4.0.8 on 2022-10-30 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rusha_applications_api', '0007_application_proxy_host_name_and_or_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='nginx_conf_path',
        ),
    ]
