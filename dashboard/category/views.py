from django.shortcuts import redirect, render
from dashboard.category.forms import CtgForm
from blog.models import Category


def ctg_list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'dashboard/category/details.html'
        ctx['ctg'] = Category.objects.get(pk=pk)
    elif delete:
        Category.objects.get(pk=delete).delete()
        return redirect('ctg_list')
    else:
        html = 'dashboard/category/list.html'
        ctx['ctg'] = Category.objects.all().order_by('-pk')
    return render(requests, html, ctx)


def ctg_add_edit(requests, pk=None):
    if pk:
        root = Category.objects.get(pk=pk)
    else:
        root = None
    form = CtgForm(instance=root)

    if requests.POST:
        forms = CtgForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('ctg_list')
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/category/forms.html', ctx)


def ctg_search(requests):
    if requests.method == 'POST':
        search = requests.POST['search']
        ctg = Category.objects.filter(name__contains=search)
        return render(requests, 'dashboard/category/list.html', {'search': search, 'ctg': ctg})
