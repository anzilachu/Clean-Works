# Generated by Django 4.2.4 on 2023-10-04 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0024_event_description_event_image_event_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attachment', models.FileField(upload_to='update-files')),
                ('Name', models.TextField(null=True)),
                ('Format', models.TextField(null=True)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.event')),
            ],
        ),
    ]