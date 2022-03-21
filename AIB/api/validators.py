from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def val_num(kods): #validate agreement number
    valid = True
    for ch in kods[0:2]:
        if not ch.isalpha():
            valid = False
    index = 2
    if not kods[index]=="-":
        if not kods[index].isalpha():
            valid = False
        index += 1
        if not kods[index]=="-":
            valid = False
    index += 1
    if not kods[index:].isnumeric():
        valid = False
    elif int(kods[index:])>999999:
        valid = False
    if not valid:
        raise ValidationError(
            _("Nepareizs numura formāts!")
        )