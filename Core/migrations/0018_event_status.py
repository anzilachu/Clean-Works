# Generated by Django 4.2.4 on 2023-09-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0017_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Status',
            field=models.IntegerField(default=1),
        ),
    ]