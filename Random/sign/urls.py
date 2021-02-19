from django.urls import path
from . import views

app_name = 'sign'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logins, name='login'),
    path('sign-up/', views.signup, name='sign-up'),
    path('auth-logouts/', views.logouts, name='logouts'),
]