# Generated by Django 4.2.4 on 2023-11-12 09:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0028_appointments_doctor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointments",
            name="Doctor",
        ),
    ]
