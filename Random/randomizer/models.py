from django.db import models


class CurrentNumber(models.Model):
    cur_numb = models.IntegerField('Текущее значение')
