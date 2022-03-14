from django.db import models

# Create your models here.

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    agreement_numurs = models.IntegerField() # 2/3 letter + "-"+ 6xdigital [0-9]
    amount = models.FloatField()
    due_to_date = models.DateField() # file_path -> i need download -> get a link
