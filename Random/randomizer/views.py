from django.shortcuts import render, redirect
from .models import CurrentNumber
from django.http import JsonResponse


def random(request):
    current = CurrentNumber.objects.get(id=1)
    context = {'cur': current.cur_numb}
    if request.is_ajax():
        return JsonResponse(context, status=200)
    return render(request, 'randomizer/random.html', context)