from django.shortcuts import render


def info(request):
    return render(request, 'contact/info.html')
