from django.db import models
# Create your models here.
from dashboard.regions import *


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    price = models.TextField(null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    project_aim = models.TextField(null=True)
    desription = models.TextField(null=True)
    file = models.FileField(null=True)
    innovastion_part = models.TextField(null=True)
    region = models.CharField(max_length=256, null=True)
    district = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
