from django.contrib import auth
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Account
from django.http import JsonResponse, request
from django.contrib.auth import authenticate
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def getProfiles(request):
    profiles = Account.objects.all()
    return JsonResponse({'profiles': list(profiles.values())})


def login_index(request):
    return render(request, 'test1.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            return HttpResponse('Hello')
        else:
            return render(request, 'test1.html')

    return HttpResponse(f'Success')
