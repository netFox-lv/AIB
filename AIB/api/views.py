from django.http import JsonResponse
from api.forms import AgreementForm
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

@api_view(['POST'])
def AddAgreement(request):
    if request.method == 'POST':#Add agreement using JSON through POST method
        form = AgreementForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            newAgreement = form.save(commit=False)
            newAgreement.document_file = request.FILES['document_file']
            newAgreement.save()
            return JsonResponse(form.data, status=201)
        else:
            return JsonResponse(form.errors, status = 400)

@api_view(['POST'])
def AddInvoice(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)#from JSON
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def GetAgreement(req, id):

    if req.method=="GET": #check if correct GET
        try:
            agr=Agreement.objects.get(id=id) #find agreement w/ id, if this fails return except
            ser=AgreementSerializer(agr)
            return Response(ser.data)
        except Agreement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def GetInvoice(request,id):
    if request.method == 'GET':
        try:
            invoice = Invoice.objects.get(id=id)
            serializer = InvoiceSerializer(invoice)
            serializer.data['document_file'] = invoice.document_file.url
            return Response(serializer.data)
        except Invoice.DoesNotExist:
            return JsonResponse(status=404)

@api_view(['GET'])
def GetLogin(req, email, passw):
    if req.method=="GET": #check if correct GET
        for user in User.objects.filter(email=email):
            if user.check_password(passw):
                login(req, user)  #<request>.user will be current user
                return JsonResponse({'access_granted':True})
        return JsonResponse({'access_granted':False})
