from django.shortcuts import render, HttpResponse, redirect
from models import *
  # the index function is called when root is visited
def index(request):
    return render(request, 'nip/login.html')

def process(request):
    pass

def strength(request):
    context = {
        'stacks': Stack.objects.all()
    }
    return render(request, 'nip/strengths.html', context)

