# Generated by Django 4.2.4 on 2023-11-12 07:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0026_clinic_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointments",
            name="Doctor",
        ),
    ]
