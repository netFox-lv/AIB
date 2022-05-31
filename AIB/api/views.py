import datetime
from logging import Filter
from django.http import HttpRequest, JsonResponse
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
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum
import os
import pytesseract
from pdf2image import convert_from_path
from dateutil import parser
import datetime


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
            agr=Agreement.objects.filter(owner=req.user).get(id=id) #find agreement w/ id, if this fails return except
            ser=AgreementSerializer(agr)
            return Response(ser.data)
        except Agreement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def GetInvoice(request,id):
    if request.method == 'GET':
        try:
            invoice = Invoice.objects.filter(owner=request.user).get(id=id)
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
                print("logging in..")
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
            data = list(Agreement.objects.filter(owner=req.user).values())
            return Response({'data': data})
        except Agreement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
@api_view(['GET'])
def getAllInvoice(req):
    if req.method=="GET": #check if correct GET
        try:
            data = list(Invoice.objects.filter(owner=req.user).values())
            return Response({'data': data})
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getRecent(req):
    if req.method == "GET":
        try:
            data = list(Invoice.objects.filter(owner=req.user).values())
            data = sorted(data, key=lambda x: x["invoice_date"],reverse=True)
            data = data[0:10]
            return Response({'data': data})
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getUnresovledInv(req):
    if req.method == "GET":
        try:
            data = Invoice.objects.filter(owner=req.user).filter(paid = False).count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getNewAgr(req):
    if req.method == "GET":
        try:
            data = Agreement.objects.filter(owner=req.user).filter(status="pending sign off").count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getFinAgr(req):
    if req.method == "GET":
        try:
            data = Agreement.objects.filter(owner=req.user).filter(status="signed").count()
            return Response({'count':data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getDrafts(req):
    if req.method == "GET":#TODO whatever needs to be done at the 4. widget
        try:
            data = Agreement.objects.filter(owner=req.user).filter(status="draft").count()
            return Response({'count':data})
        except:
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
                .filter(owner=req.user)
                .filter(invoice_date__lt=datetime.date(currYear,i+1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
                else:
                    data.append([i,(Invoice.objects.all()
                .filter(owner=req.user)
                .filter(invoice_date__lt=datetime.date(currYear+1,1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
            currYear += 1#back to the present year
            for i in range(1,currMonth+1):#all this year's months before current(never going to visit 12)
                data.append([i,(Invoice.objects.all()
                .filter(owner=req.user)
                .filter(invoice_date__lt=datetime.date(currYear,i+1,1))#invoices before the next month's first day(less than)
                .filter(invoice_date__gte=datetime.date(currYear,i,1))#invoices in this month's first day or later(greater or equal)
                .aggregate(Sum('amount')))['amount__sum']])
            
            return Response({'data':data})
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def AddPdf(request):

    if request.method == 'POST':#Add agreement using JSON through POST method
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdfurl=serializer.data.get('pdf')
            pdfnam=serializer.data.get('name')
            pdfurl=pdfurl[pdfurl.rfind('/')+1:-4]
            pages = convert_from_path(os.path.abspath(os.path.dirname(__name__))+os.path.normcase(serializer.data.get('pdf')),poppler_path=(os.path.dirname(__name__)+"poppler-0.68.0//bin"))
            (pages[0]).save(os.path.dirname(__name__)+"temp/temp_"+pdfnam+"_"+pdfurl+".jpg", 'JPEG')
            s = pytesseract.image_to_string(os.path.dirname(__name__)+"temp/temp_"+pdfnam+"_"+pdfurl+".jpg", config=r'--oem 3 --psm 6')
            os.remove(os.path.dirname(__name__)+"temp/temp_"+pdfnam+"_"+pdfurl+".jpg")

            vatp=s.rfind("VAT")

            s=s.lower()
            finds=s.find("invoice number ")
            if (finds>0):
                finde=s.find("\n", finds+1)
                finds=s.rfind(" ",0,finde-1)+1
                inum=s[finds:finde]
            else:inum=""

            finds=s.find("invoice date")
            if (finds>0):
                finde=s.find("\n", finds+1)
                finds=s.find(" ",finds+11)+1
                idats=s[finds:finde]
            else:idats=""
            idat=parser.parse(idats)
            if (idat.day<=15):
                pdat=idat-datetime.timedelta(weeks = 3)
            else:
                pdat=idat

            finds=s.find("due date")
            if (finds>0):
                finde=s.find("\n", finds+1)
                finds=s.find(" ",finds+7)+1
                ddats=s[finds:finde]
            else:ddats=""
            ddat=parser.parse(ddats)


            keyset=["sum", "total", "amount", "papildinat_in_lowercase"]
            finde=s.find("\n", vatp+1)
            corrkey="null"
            for key in keyset:
                if ((s.find(key,finde))>0):
                    corrkey=key
                    break
            finds=s.find(corrkey,finde)
            finde=s.find("\n", finds+1)
            if (finds>0):
                finde=s.find("\n", finds+1)
                amou=s[finde-1:finde]
                while (not(amou.isdigit())):
                    finde=s.rfind(" ",0,finde-1)
                    amou=s[finde-1:finde]
                finds=s.rfind(" ",0,finde-1)-1
                amou=s[finds:finds+1]
                while (amou.isdigit()):
                    finds=s.rfind(" ",0,finds-1)-1
                    amou=s[finds:finds+1]
                amou=s[finds+2:finde]
            else:amou=""

            #return JsonResponse(s, status=201, safe=False)

            return JsonResponse({
                                    "invoice_number": inum,
                                    "amount": amou,
                                    "invoice_date": idat,
                                    "payment_to_date": ddat,
                                    'payment_period_month': pdat.month,
                                    'payment_period_year': pdat.year,
                                    'paid': False,
                                    'pdf': serializer.data.get('pdf'),
                                }, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)            

@api_view(['GET'])
def getProgress(req):
    if req.method == "GET":
        try:
            invoiceSum = Invoice.objects.all().filter(owner=req.user).filter(payment_method='by agreement').filter(paid=True).aggregate(Sum('amount'))['amount__sum']
            agreementSum = Agreement.objects.all().filter(owner=req.user).filter(status='signed').aggregate(Sum('amount'))['amount__sum']
            return Response({'earned':invoiceSum,'total':agreementSum})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getLoginInfo(req):
    if req.method == "GET":
        try:
            if req.user.is_authenticated:
                return Response({'logged_in':True,'username':req.user.username})
            else:
                return Response({'logged_in':False})
        except:
            return Response({'logged_in':False},status=400)

@api_view(['GET'])
def getLogout(req):
    try:
        logout(req)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=401)