from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.

def AddAgreement(request):
    
    if request.method == 'POST':#Add agreement using JSON through POST method
        data = JSONParser().parse(request)#from JSON
        serializer = AgreementSerializer(data=data)#into table
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)#failed to reckognize data 