import pytest

from extraction.models import (
    JobStatus
)


@pytest.mark.django_db
def test_cancel_pending_job(
    client,
    pending_job
):

    response = client.post(
        f"/api/v1/scan/cancel/{pending_job.id}"
    )

    assert response.status_code == 200

    pending_job.refresh_from_db()

    assert (
        pending_job.status
        ==
        JobStatus.CANCELLED
    )
