from django.shortcuts import redirect, render

from dashboard.project.forms import ProjectForm
from blog.models import Project


# function to delete/view List/view Detail
def project_list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'admin/project/details.html'
        ctx['project'] = Project.objects.get(pk=pk)
    elif delete:
        Project.objects.get(pk=delete).delete()
        return redirect('project_list')
    else:
        html = 'admin/project/list.html'
        ctx['project'] = Project.objects.all().order_by('-pk')
    return render(requests, html, ctx)


# function to add or edit to Project model
def project_add_edit(requests, pk=None):
    if pk:
        root = Project.objects.get(pk=pk)
    else:
        root = None
    form = ProjectForm(instance=root)

    if requests.POST:
        forms = ProjectForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('project_list')
    ctx = {
        'form': form
    }
    return render(requests, 'admin/project/forms.html', ctx)


# Search function
def search(requests):
    if requests.method == 'POST':
        search = requests.POST['search']
        project = Project.objects.filter(name__contains=search)
        return render(requests, 'admin/project/list.html', {'search': search, 'project': project})
