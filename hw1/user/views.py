from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, redirect, render
from django.http import JsonResponse
from .models import User
# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'username': user.username, 'type': user.type})
        return JsonResponse({'success': False})


def register(request):
    if request.method == 'POST':
        user = User(username=request.POST['username'], type=request.POST['type'])
        user.set_password(request.POST['password'])
        user.save()
        return JsonResponse({'success': True})

