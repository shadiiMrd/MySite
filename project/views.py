from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .filters import *


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project/detail.html' ,
                  {'project': project})

def list(request):
    projects = Project.objects.all()

    filter = ProjectFilter(request.GET, queryset=projects)
    projects = filter.qs

    paginator = Paginator(projects, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'project/list.html',
                  {'projects': projects , 'page_num':page_num,'page_obj': page_obj})
