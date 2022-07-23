from email import message
from email.quoprimime import body_check
from pickle import TRUE
from turtle import title
from django.db import models

# to auto increment the id
import uuid 

# Create your models here.

class about(models.Model):
    body = models.TextField(null=True, blank=True)
    # thumbnail = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body

class mySkill(models.Model):
    # title = models.CharField(max_length=100, null=True)
    skills = models.PositiveIntegerField(null=True)
    thumbnail = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


class service(models.Model):
    title = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class contact(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.fName} {self.lName}"
