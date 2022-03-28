from django.db import models
from api.validators import val_period
from api.validators import val_num
# Create your models here.

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    agreement_numurs = models.TextField(unique=True,validators=[val_num]) # 2/3 letter + "-"+ 6xdigital [0-9] 
    amount = models.FloatField()
    due_to_date = models.DateField()
    #access_path = models.FilePathField(path="/agreements")# file_path -> i need download -> get a link

class Invoice(models.Model):
    id = models.IntegerField(primary_key=True)
    invoice_number = models.TextField(unique=True,validators=[val_num])
    amount = models.FloatField()
    invoice_date = models.DateField()
    payment_to_date = models.DateField()
    payment_period = models.TextField(validators=[val_period])
    #payment_period_month
    #payment_period_year
    #paid: bool