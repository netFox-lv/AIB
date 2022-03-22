from django.db import models
from api.validators import val_num
# Create your models here.

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    agreement_numurs = models.TextField(unique=True,validators=[val_num]) # 2/3 letter + "-"+ 6xdigital [0-9] 
    amount = models.FloatField()
    due_to_date = models.DateField()
    #access_path = models.FilePathField(path="/agreements")# file_path -> i need download -> get a link
