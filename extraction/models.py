import uuid

from django.db import models


class JobStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"
    CANCELLED = "cancelled", "Cancelled"


class ExtractionJob(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    status = models.CharField(
        max_length=30,
        choices=JobStatus.choices,
        default=JobStatus.PENDING
    )

    api_token = models.TextField()

    record_count = models.IntegerField(default=0)

    error_message = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    started_at = models.DateTimeField(
        blank=True,
        null=True
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)


class ExtractedRecord(models.Model):
    job = models.ForeignKey(
        ExtractionJob,
        on_delete=models.CASCADE,
        related_name="records"
    )

    external_id = models.CharField(
        max_length=255
    )

    email = models.EmailField()

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email
