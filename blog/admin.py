from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Comments)

