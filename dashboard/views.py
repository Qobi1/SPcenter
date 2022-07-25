from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def admin_index(requests):
    return render(requests, 'dashboard/admin-index.html')

