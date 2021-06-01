from django.contrib import admin

from import_export.admin import ImportExportMixin
from import_export_celery.admin_actions import (
    create_export_job_action,
)

from . import models


@admin.register(models.Kol)
class KolAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'first_name',
        'middle_name',
        'last_name',
        'credential',
        'specialty',
    )

    actions = (create_export_job_action,)