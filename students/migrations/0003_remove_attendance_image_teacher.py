# Generated by Django 3.0.7 on 2020-06-27 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_attendance_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance_image',
            name='teacher',
        ),
    ]
