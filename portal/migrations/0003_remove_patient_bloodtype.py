# Generated by Django 4.1.3 on 2022-11-27 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_patient_patientidtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Bloodtype',
        ),
    ]
