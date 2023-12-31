# Generated by Django 4.2.4 on 2023-11-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0030_appointments_doctor"),
    ]

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
                ("Status", models.IntegerField(default=1)),
                ("number", models.CharField(max_length=15)),
                ("service", models.CharField(max_length=50)),
                ("message", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="album",
            name="AddedBy",
        ),
        migrations.RemoveField(
            model_name="album",
            name="EditedBy",
        ),
        migrations.RemoveField(
            model_name="album_image",
            name="Album",
        ),
        migrations.DeleteModel(
            name="Application",
        ),
        migrations.RemoveField(
            model_name="appointments",
            name="Clinic",
        ),
        migrations.RemoveField(
            model_name="appointments",
            name="Department",
        ),
        migrations.RemoveField(
            model_name="appointments",
            name="Doctor",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="AddedBy",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="EditedBy",
        ),
        migrations.RemoveField(
            model_name="career",
            name="AddedBy",
        ),
        migrations.RemoveField(
            model_name="career",
            name="Clinic",
        ),
        migrations.RemoveField(
            model_name="career",
            name="EditedBy",
        ),
        migrations.RemoveField(
            model_name="clinic",
            name="AddedBy",
        ),
        migrations.RemoveField(
            model_name="clinic",
            name="EditedBy",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="AddedBy",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="Clinic",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="Department",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="EditedBy",
        ),
        migrations.DeleteModel(
            name="Enquiry",
        ),
        migrations.RemoveField(
            model_name="event_attachments",
            name="Event",
        ),
        migrations.RemoveField(
            model_name="expertise",
            name="Doctor",
        ),
        migrations.RemoveField(
            model_name="institution",
            name="Doctor",
        ),
        migrations.DeleteModel(
            name="Newslatter",
        ),
        migrations.DeleteModel(
            name="Uploades",
        ),
        migrations.DeleteModel(
            name="Album",
        ),
        migrations.DeleteModel(
            name="Album_image",
        ),
        migrations.DeleteModel(
            name="Appointments",
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.DeleteModel(
            name="Career",
        ),
        migrations.DeleteModel(
            name="Clinic",
        ),
        migrations.DeleteModel(
            name="Department",
        ),
        migrations.DeleteModel(
            name="Doctor",
        ),
        migrations.DeleteModel(
            name="Event",
        ),
        migrations.DeleteModel(
            name="Event_Attachments",
        ),
        migrations.DeleteModel(
            name="Expertise",
        ),
        migrations.DeleteModel(
            name="Institution",
        ),
    ]
