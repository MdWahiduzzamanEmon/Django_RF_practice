from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from FirstApp.models import userContact
from FirstApp.serializers import userContactSerializer

# Create your views here.

@csrf_exempt
def getUserInfo(request):
    if request.method == 'GET':
        getUserInfoObj = userContact.objects.all()
        serializer = userContactSerializer(getUserInfoObj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

