from django.contrib import admin

from .models import (
    ExtractionJob,
    ExtractedRecord
)


@admin.register(ExtractionJob)
class ExtractionJobAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "status",
        "record_count",
        "created_at",
    )

    search_fields = (
        "id",
        "status",
    )


@admin.register(ExtractedRecord)
class ExtractedRecordAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "first_name",
        "last_name",
    )
