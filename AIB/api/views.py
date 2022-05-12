import datetime
from logging import Filter
from django.http import JsonResponse
from api.forms import AgreementForm
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

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

@api_view(['POST'])
def Login(req):
    if req.method=="POST": #check if correct method
        try:
            username = User.objects.get(email=req.data['email'])
            password = req.data['password']
            user = authenticate(req, username=username, password= password)
            if user is not None:
                login(req,user)
                print("user logged in:",user)
                return Response({'access_granted':True})
            else:
                return Response({'access_granted':False})
        except:
            return Response(status=401)

@api_view(['GET'])
def getAllAgreements(req):
    if req.method=="GET": #check if correct GET
        try:
            data = list(Agreement.objects.values())
            return Response({'data': data})
        except Agreement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
@api_view(['GET'])
def getAllInvoice(req):
    if req.method=="GET": #check if correct GET
        try:
            data = list(Invoice.objects.values())
            return Response({'data': data})
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getRecent(req):
    if req.method == "GET":
        try:
            data = list(Invoice.objects.values())
            data = sorted(data, key=lambda x: x["invoice_date"],reverse=True)
            data = data[0:10]
            return Response({'data': data})
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getUnresovledInv(req):
    if req.method == "GET":
        try:
            data = Invoice.objects.filter(paid = False).count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getNewAgr(req):
    if req.method == "GET":
        try:
            data = Agreement.objects.filter(status="pending sign off").count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getFinAgr(req):
    if req.method == "GET":
        try:
            data = Agreement.objects.filter(status="finished").count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getDrafts(req):
    if req.method == "GET":#TODO whatever needs to be done at the 4. widget
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getIncomePerMonth(req):
    if req.method == "GET":
        try:
            data = []
            today = datetime.datetime.today()
            currMonth = today.month
            currYear = today.year
            currYear = currYear-1#go back a year
            for i in range(currMonth+1,13):#months from the previous year within a year of current
                if not i==12:#have to take next january of year for next date if it's december
                    data.append([i,(Invoice.objects.all()
                .filter(invoice_date__lt=datetime.date(currYear,i+1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
                else:
                    data.append([i,(Invoice.objects.all()
                .filter(invoice_date__lt=datetime.date(currYear+1,1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
            currYear += 1#back to the present year
            for i in range(1,currMonth+1):#all this year's months before current(never going to visit 12)
                data.append([i,(Invoice.objects.all()
                .filter(invoice_date__lt=datetime.date(currYear,i+1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
            
            return Response({'data':data})
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getProgress(req):
    if req.method == "GET":
        try:
            return
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getLoginInfo(req):
    print(req.user)
    if req.method == "GET":
        try:
            if req.user.is_authenticated:
                return Response({'logged_in':True,'username':req.user.username})
            else:
                return Response({'logged_in':False})
        except Exception as e:
            print()
            print(e)
            print()
            return Response({'logged_in':False},status=400)

@api_view(['GET'])
def logout(req):
    if req.method == "GET":
        try:
            print("logging out user ",req.user)
            logout(req.user)
        except Exception as e:
            Response({'err': e})