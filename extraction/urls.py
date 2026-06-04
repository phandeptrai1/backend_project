from django.urls import path

from .views import (
    HealthView,
    StartScanView,
    JobStatusView,
    ResultView,
    CancelJobView,
    RemoveJobView,
    JobListView,
    StatisticsView,
)

urlpatterns = [
    path(
        "scan/start",
        StartScanView.as_view()
    ),

    path(
        "scan/status/<uuid:job_id>",
        JobStatusView.as_view()
    ),

    path(
        "scan/result/<uuid:job_id>",
        ResultView.as_view()
    ),

    path(
        "scan/cancel/<uuid:job_id>",
        CancelJobView.as_view()
    ),

    path(
        "scan/remove/<uuid:job_id>",
        RemoveJobView.as_view()
    ),

    path(
        "jobs/jobs",
        JobListView.as_view()
    ),

    path(
        "jobs/statistics",
        StatisticsView.as_view()
    ),

    path(
        "health",
        HealthView.as_view()
    ),
]
