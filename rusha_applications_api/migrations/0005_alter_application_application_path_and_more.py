# Generated by Django 4.0.8 on 2022-10-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusha_applications_api', '0004_alter_application_application_domain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_path',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_port',
            field=models.IntegerField(unique=True),
        ),
    ]
