from dataclasses import fields
from api.models import Invoice
from rest_framework import serializers

from api.models import Agreement

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = (
        'id',
        'agreement_numurs',
        'amount',
        'customer',
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
            'amount',
            'invoice_date',
            'payment_to_date',
            'payment_period_month',
            'payment_period_year',
            'paid',
        )