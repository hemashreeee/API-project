from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import api_data

# Register your models here.
@admin.register(api_data)
class api_data(ImportExportModelAdmin):
    pass