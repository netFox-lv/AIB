from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def val_num(kods): #validate agreement number
    if not (re.match(r"^[:alpha:][:alpha:]-\d\d\d\d\d\d$", kods) 
    or re.match(r"^[:alpha:][:alpha:][:alpha:]-\d\d\d\d\d\d$", kods)):
        raise ValidationError(
            _("Nepareizs numura formāts!")
        )

def val_period(periods):
    if not (re.match(r'^Q[1-4]-\d\d\d\d$', periods) or re.match(r'^\d\d-\d\d\d\d$', periods)):
        raise ValidationError(
            _("Nepareizs periods!")
        )