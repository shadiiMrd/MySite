from django.shortcuts import render

from project.models import Project


def main(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html' ,
                  {'projects': projects})