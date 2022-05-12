from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from AIB.settings import BASE_DIR
from api.validators import val_num
# Create your models here.

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    agreement_numurs = models.TextField(unique=True,validators=[val_num]) # 2/3 letter + "-"+ 6xdigital [0-9] 
    amount = models.FloatField()
    customer = models.TextField()
    owner = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    due_to_date = models.DateField()
    status = models.TextField(default="pending sign off")
    document_file = models.FileField(upload_to = "agreements", blank=True)# file_path -> i need download -> get a link

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    class paymentMethods(models.TextChoices):
            ONLINE = 'Online'
            ON__DELIVERY = 'Cash on delivery'
            BEFORE_DELIVERY = 'Cash before delivery'
    invoice_number = models.TextField(unique=True,validators=[val_num])
    customer = models.TextField()
    owner = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    amount = models.FloatField()
    invoice_date = models.DateField()
    payment_method = models.TextField(choices=paymentMethods.choices, default=paymentMethods.ONLINE)
    payment_to_date = models.DateField()
    payment_period_month = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    payment_period_year = models.PositiveIntegerField()
    paid = models.BooleanField()