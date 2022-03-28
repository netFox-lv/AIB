from api.models import Invoice
from rest_framework import serializers

from api.models import Agreement

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ('id',
        'agreement_numurs',
        'amount',
        'due_to_date',
        #'access_path'
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
            'payment_period'
        )