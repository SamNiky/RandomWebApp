from celery import shared_task
from .models import CurrentNumber
from random import randint

@shared_task
def createnumber():
    answer = randint(1, 10000)
    create = CurrentNumber.objects.get(id=1)
    create.cur_numb = answer
    create.save()