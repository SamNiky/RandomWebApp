from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'sign/index.html')

def login(request):
    return HttpResponse("login page")

def signup(request):
    return HttpResponse("sign-up page")