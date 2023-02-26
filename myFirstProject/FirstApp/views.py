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
    #    //check name already exists
        try:
            userContact.objects.get(name=data['name'])
            return HttpResponse(status=400, content="User already exists")
        except userContact.DoesNotExist:
            serializer = userContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        

# put and delete methods

@csrf_exempt
def getUserInfoDetail(request, pk):

    try:
        snippet = userContact.objects.get(pk=pk)
    except userContact.DoesNotExist:
        return HttpResponse(status=404, content="User not found")

    if request.method == 'GET':
        serializer = userContactSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userContactSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            JsonResponse(serializer.data)
            return HttpResponse(status=200, content="User updated")
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204, content="User deleted")
