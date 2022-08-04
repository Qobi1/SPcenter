from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# from config.settings import LOGIN_URL


@login_required
def admin_index(requests):
    return render(requests, 'admin/admin-index.html')
