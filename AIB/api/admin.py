from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Agreement)
admin.site.register(Invoice)
admin.site.register(UploadPdf)