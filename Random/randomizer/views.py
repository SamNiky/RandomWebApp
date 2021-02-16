from django.shortcuts import render, redirect
from django.http import HttpResponse
from .engine import randomInt
import time

def random(request):
    a = randomInt()
    time.sleep(5)
    return HttpResponse(a)


