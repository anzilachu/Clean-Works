# Generated by Django 4.2.4 on 2023-08-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_department_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='Location',
        ),
        migrations.AddField(
            model_name='career',
            name='Clinic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.clinic'),
            preserve_default=False,
        ),
    ]
