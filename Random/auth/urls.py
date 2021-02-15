from django.urls import path
from . import views

app_name = 'auth'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('sign-out/', views.signOut, name='sign-out'),
]