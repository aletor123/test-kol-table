# # myapp/admin.py
# from django.contrib import admin
# from data_wizard.admin import ImportActionModelAdmin
#
# from .models import FileModel
#
#
# @admin.register(FileModel)
# class FileModelAdmin(ImportActionModelAdmin):
#     pass
from django.contrib import admin

from . import models


@admin.register(models.Kol)
class KolAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'credential',
        'specialty',
    )