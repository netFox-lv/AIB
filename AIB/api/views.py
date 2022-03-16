from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def AddAgreement(request):
    
    if request.method == 'POST':#Add agreement using JSON through POST method
        data = JSONParser().parse(request)#from JSON
        serializer = AgreementSerializer(data=data)#into table
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)#failed to reckognize data 


@api_view(['GET'])
def GetAgreement(req, id):

    if req.method=="GET": #check if correct GET
        try:
            agr=Agreement.objects.get(id=id) #find agreement w/ id, if this fails return except
            ser=AgreementSerializer(agr)
            return Response(ser.data)
        except Agreement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)