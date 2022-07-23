# Generated by Django 4.2.dev20220603193729 on 2022-06-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_services_thumbnail_alter_contact_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='myskills',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]