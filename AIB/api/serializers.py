from rest_framework import serializers

from .models import Agreement

class AgreementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agreement
        fields = ('id','agreement_numurs','amount','due_to_date')