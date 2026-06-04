import pytest


@pytest.mark.django_db
def test_job_not_found(client):

    response = client.get(
        "/api/v1/scan/status/"
        "11111111-1111-1111-1111-111111111111"
    )

    assert response.status_code == 404
