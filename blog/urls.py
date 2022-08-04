from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/<int:pk>/', about, name='about'),
    path('projects/<int:pk>/', projects, name='projects'),
    path('search-ctg/', index_search, name='index_search'),
    path('search/', projects_search, name='project_searching'),
]