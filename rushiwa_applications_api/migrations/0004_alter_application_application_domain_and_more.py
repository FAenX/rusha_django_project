# Generated by Django 4.0.8 on 2022-10-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rushiwa_applications_api', '0003_rename_applocation_domain_application_application_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_domain',
            field=models.CharField(default=3000, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='application_host',
            field=models.CharField(default=3000, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='application_path',
            field=models.CharField(default=3000, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='application_port',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
    ]
