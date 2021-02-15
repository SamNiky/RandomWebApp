from django.shortcuts import render
from django.http import HttpResponse

def random(request):
    return HttpResponse(" Page with randomizer ")
