import pytest


@pytest.mark.django_db
def test_start_scan(client):

    response = client.post(
        "/api/v1/scan/start",
        {
            "api_token": "token123"
        },
        content_type="application/json"
    )

    assert response.status_code == 202

    assert "job_id" in response.json()
