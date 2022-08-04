from django.shortcuts import redirect, render
from dashboard.person.forms import PersonForm
from blog.models import Person


# function to view the list/detail or delete
def person_list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'admin/person/details.html'
        ctx['person'] = Person.objects.get(pk=pk)
    elif delete:
        Person.objects.get(pk=delete).delete()
        return redirect('person_list')
    else:
        html = 'admin/person/list.html'
        ctx['person'] = Person.objects.all().order_by('-pk')
    return render(requests, html, ctx)


# function to add/edit in Person model
def person_add_edit(requests, pk=None):
    if pk:
        root = Person.objects.get(pk=pk)
    else:
        root = None
    form = PersonForm(instance=root)

    if requests.POST:
        forms = PersonForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('person_list')
    ctx = {
        'form': form
    }
    return render(requests, 'admin/person/forms.html', ctx)


# function to search a particular input
def person_search(requests):
    if requests.method == 'POST':
        search = requests.POST['search']
        person = Person.objects.filter(first_name__contains=search)
        return render(requests, 'admin/person/list.html', {'search': search, 'person': person})
