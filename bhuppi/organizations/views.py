from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Organization
from accounts.models import User
import json

@require_POST
def create(request):
    if not request.user.is_superuser:
        return JsonResponse({'message': 'Super User access is required'}, status=403)
    json_data = json.loads(request.body)
    org = Organization(name=json_data['name'])
    if 'super_admin_user_id' in json_data:
        org.super_admin = User.objects.get(id=json_data['super_admin_user_id'])
    org.save()
    org = Organization.objects.get(id=org.id)
    return JsonResponse({'organization': (org.serialize)}, safe=False)

def read(request, id):
    org = Organization.objects.get(id=id)
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            return JsonResponse({'message': 'Super User access is required'}, status=403)
        org.delete()
        return JsonResponse({'status': '200'})
    elif request.method == 'PATCH':
        if request.user.is_superuser:
            return JsonResponse({'message': 'Super User access is required'}, status=403)
        json_data = json.loads(request.body)
        if 'super_admin_user_id' in json_data:
            org.super_admin = User.objects.get(id=json_data['super_admin_user_id'])
            org.save()
    else:
        return JsonResponse({'message': 'Method Not Allowed'}, status=405)
    return JsonResponse({'organization': (org.serialize)}, safe=False)
