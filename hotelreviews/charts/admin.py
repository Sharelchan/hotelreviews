from django.contrib import admin
from .models import Data
from .models import wordcloud
from import_export.admin import ImportExportModelAdmin

class DataImportExportAdmin(ImportExportModelAdmin):
    list_display = ('hotel_name','hotel_location','rating','review')

admin.site.register(Data, DataImportExportAdmin)
admin.site.register(wordcloud)

# Register your models here.
