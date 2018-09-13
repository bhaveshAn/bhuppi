from django.shortcuts import render, get_object_or_404
from .models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

@require_POST
def signup(request):
    json_data = json.loads(request.body)
    username = json_data['username']
    password = json_data['password']
    is_user_exists = User.objects.filter(username=username)
    if is_user_exists:
         return JsonResponse({"message": 'User already exists'}, safe=False)    
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return JsonResponse({"message": 'User successfully created'}, safe=False)    

@require_POST
def login_user(request):
    json_data = json.loads(request.body)
    username = json_data['username']
    password = json_data['password']
    user = get_object_or_404(User, username=username)
    auth_login(request, user)
    return JsonResponse({'message': 'User Successfully Logged In','user': str(user)}, status=200)

@require_GET
def logout_view(request):
    if request.user.is_authenticated():
        auth_logout(request) 
    return JsonResponse({'message': 'User Successfully Logged Out'}, status=200)

@login_required
def add_super_admin(request):
    #curr_user = User.objects.get(id=request.user.id)
    if not request.user.is_superuser:
        JsonResponse({'message': 'Super User access is required'}, status=403)
       
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return JsonResponse({"message": 'User successfully created'}, safe=False)
