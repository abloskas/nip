from django.shortcuts import render, HttpResponse, redirect
from models import *
  # the index function is called when root is visited
def index(request):
    return render(request, 'nip/login.html')

def process(request):
    pass

def strength(request):
    return render(request, 'nip/strengths.html')

def user_result(request):
    return render(request, 'nip/user_search.html')

def help_result(request):
    return render(request, 'nip/help_search.html')