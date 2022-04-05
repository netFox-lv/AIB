from api.models import Agreement
from django.forms import ModelForm

class AgreementForm(ModelForm):
    class Meta:
        model = Agreement
        fields = ('id',
        'agreement_numurs',
        'amount',
        'due_to_date',
        'document_file'
        )
