# Generated by Django 4.2.4 on 2023-09-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0018_event_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=225)),
                ('File', models.FileField(upload_to='files')),
            ],
        ),
    ]
