# Generated by Django 4.2.dev20220603193729 on 2022-06-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_service_rename_aboutme_about_rename_myskills_myskill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
