# Generated by Django 4.0.8 on 2022-10-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusha_applications_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_host',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='application_path',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='application_port',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='applocation_domain',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
