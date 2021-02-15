from django.urls import path
from . import views

app_name = 'randomizer'
urlpatterns = [
    path('', views.random, name='random')
]