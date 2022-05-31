from dataclasses import fields
from api.models import Invoice
from rest_framework import serializers

from api.models import Agreement, UploadPdf

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = (
        'id',
        'agreement_numurs',
        'amount',
        'customer',
        'owner',
        'due_to_date',
        'status',
        'document_file'
        )

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields =(
            'id',
            'invoice_number',
            'customer',
            'owner',
            'amount',
            'invoice_date',
            'payment_method',
            'payment_to_date',
            'payment_period_month',
            'payment_period_year',
            'paid',
        )
        
class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPdf
        fields = (
            'name',
            'pdf',
        )