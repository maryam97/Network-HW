from django.shortcuts import render, get_list_or_404, redirect
from django.http import JsonResponse
from .models import Receipt
from user.models import User
# Create your views here.


def receive(request):
    if request.method == 'POST':
        if request.user.type == 'pharmacy':
            user = request.POST['username']
            patient_descs = Receipt.objects.filter(user=User.objects.get(username=user)).order_by('-created_at').first()
            return JsonResponse({'desc': patient_descs.rec, 'user': patient_descs.user.username})


def add(request):
    if request.method == 'POST':
        if request.user.type == 'doctor':
            user = request.POST['username']
            desc = request.POST['description']
            rec = Receipt(rec=desc, user=User.objects.get(username=user))
            rec.save()
            return JsonResponse({'success': True})


def history(request):
    if request.method == 'POST':
        if request.user.type == 'patient':
            user = request.POST['username']
            patient_descs = Receipt.objects.filter(user=User.objects.get(username=user)).all()
            desc = [{'desc': _.rec, 'user': _.user.username} for _ in patient_descs]
            return JsonResponse({'history': desc})
