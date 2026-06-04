from django.utils import timezone

from .models import ExtractionJob
from .models import ExtractedRecord
from .models import JobStatus


class ExtractionService:

    @staticmethod
    def start_job(api_token: str):

        job = ExtractionJob.objects.create(
            api_token=api_token,
            status=JobStatus.IN_PROGRESS,
            started_at=timezone.now()
        )

        for i in range(100):
            ExtractedRecord.objects.create(
                job=job,
                external_id=str(i),
                email=f"user{i}@example.com",
                first_name=f"User{i}",
                last_name="Test"
            )

        job.record_count = 100
        job.status = JobStatus.COMPLETED
        job.completed_at = timezone.now()

        job.save()

        return job
