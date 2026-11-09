from django.shortcuts import render


def myStory(request):
    return render(request, 'about/my_story.html')


def skill(request):
    return render(request, 'about/skill.html')

def education(request):
    return render(request, 'about/education.html')

