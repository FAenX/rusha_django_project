# Generated by Django 4.0.8 on 2022-10-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rushiwa_applications_api', '0006_remove_application_application_domain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='proxy_host_name_and_or_port',
            field=models.CharField(max_length=200, null=True),
        ),
    ]