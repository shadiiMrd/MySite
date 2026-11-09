from django.shortcuts import render

def list(request):
    return render(request,'experience/list.html')