# Generated by Django 4.2.dev20220603193729 on 2022-06-15 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_myskill_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myskill',
            name='title',
        ),
    ]
