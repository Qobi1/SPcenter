from django.db import models
# Create your models here.
from dashboard.regions import *


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    project_aim = models.TextField()
    desription = models.TextField()
    file = models.FileField()
    innovastion_part = models.TextField()
    region = models.CharField(choices=get_region(), max_length=256)
    district = models.CharField(choices=get_district(1), max_length=256)

    def __str__(self):
        return self.name


class Comments(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
