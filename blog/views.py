from contextlib import closing

from django.db import connection
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
# Create your views here.


def index(requests):
    query = Project.objects.all()
    ctg = Category.objects.all()
    return render(requests, 'index.html', {'query': query, 'ctg': ctg})


def about(requests, pk):
    query = Project.objects.get(pk=pk)
    if requests.POST:
        comm = Comments()
        comm.text = requests.POST.get('text', '')
        comm.project = query
        comm.save()
        # return render(requests, 'about.html')
        return redirect('index')
    comment = Comments.objects.filter(project_id=pk)
    return render(requests, 'about.html', {'query': query, 'comment': comment})


def projects(requests, pk):
    query = Project.objects.filter(category_id_id=pk)
    ctg = Category.objects.all()
    return render(requests, 'projects.html', {'ctg': ctg, 'query': query})


# searching specific info
def index_search(requests):
    if requests.method == 'POST':
        search = requests.POST['search']
        project = Project.objects.filter(name__contains=search)
        return render(requests, 'index.html', {'query': project, 'search': search})


# searching specific info
def projects_search(requests):
    if requests.method == 'POST':
        search = requests.POST['search']
        print(search)
        project = Project.objects.filter(name__icontains=search)
        return render(requests, 'projects.html', {'query': project, 'search': search})