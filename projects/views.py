from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def projects(request):
    return render(request, 'projects.html')

def project(request, pk):
    return HttpResponse("SINGLE PROJECT" + ' ' + str(pk))
