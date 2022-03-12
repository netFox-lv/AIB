from django.db import models

# Create your models here.

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    agreement_numurs = models.IntegerField()
    amount = models.FloatField()
    due_to_date = models.DateField()
