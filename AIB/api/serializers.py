from rest_framework import serializers

from api.models import Agreement

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ('id',
        'agreement_numurs',
        'amount',
        'due_to_date')