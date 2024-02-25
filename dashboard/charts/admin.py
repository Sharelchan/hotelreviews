from django.contrib import admin
from .models import Data
from import_export.admin import ImportExportModelAdmin

class DataImportExportAdmin(ImportExportModelAdmin):
    list_display = ('hotel_name','price','rating','review')

admin.site.register(Data, DataImportExportAdmin)

# Register your models here.
