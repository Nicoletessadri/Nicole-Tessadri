# Generated by Django 4.2.4 on 2023-09-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicaODON', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='camada',
        ),
    ]
