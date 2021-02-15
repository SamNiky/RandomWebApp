from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse(" Login page ")

def signUp(request):
    return HttpResponse(" Sign-Up page ")

def SignOut(request):
    return HttpResponse(" Sign-Out page ")