# Generated by Django 4.2.4 on 2023-11-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactFormSubmission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("number", models.CharField(max_length=15)),
                ("service", models.CharField(max_length=50)),
                ("message", models.TextField()),
            ],
        ),
    ]
