import pytest

from extraction.models import (
    ExtractionJob,
    JobStatus
)


@pytest.fixture
def completed_job():

    return ExtractionJob.objects.create(
        api_token="abc",
        status=JobStatus.COMPLETED,
        record_count=10
    )


@pytest.fixture
def pending_job():

    return ExtractionJob.objects.create(
        api_token="abc",
        status=JobStatus.PENDING
    )
