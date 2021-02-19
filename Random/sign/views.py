from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('/random')
    return render(request, 'sign/index.html')

def logins(request):
    if request.user.is_authenticated:
        return redirect('/random')
    context = {}
    if request.method == 'POST':
        user = request.POST.get('username')
        user_pass = request.POST.get('password')
        auth = authenticate(request, username=user, password=user_pass)
        if auth is not None:
            login(request, auth)
            return redirect('/random')
        else:
            context['error'] = "неправильный логин или пароль"
    return render(request, 'sign/login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/random')
    if request.is_ajax():
        user = request.GET.get('user_name')
        if User.objects.filter(username=user).exists():
            return JsonResponse({'ans': 1}, status=200)
        else:
            return JsonResponse({'ans': 0}, status=200)
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {'form': form}
    return render(request, 'sign/signup.html', context)

def logouts(request):
    logout(request)
    return redirect('/')