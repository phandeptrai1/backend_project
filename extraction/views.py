from django.db.models import Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import ExtractionJob
from .models import ExtractedRecord
from .models import JobStatus

from .serializers import (
    StartScanSerializer,
    JobSerializer,
    RecordSerializer,
)

from .services import ExtractionService
from .pagination import ResultPagination
class HealthView(APIView):

    def get(self, request):
        return Response({
            "status": "ok"
        })
class StartScanView(APIView):

    def post(self, request):

        serializer = StartScanSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        job = ExtractionService.start_job(
            serializer.validated_data["api_token"]
        )

        return Response(
            {
                "job_id": str(job.id)
            },
            status=status.HTTP_202_ACCEPTED
        )
class JobStatusView(APIView):

    def get(self, request, job_id):

        try:
            job = ExtractionJob.objects.get(
                pk=job_id
            )
        except ExtractionJob.DoesNotExist:
            return Response(
                {
                    "detail": "Job not found"
                },
                status=404
            )

        return Response(
            JobSerializer(job).data
        )
class ResultView(ListAPIView):

    serializer_class = RecordSerializer
    pagination_class = ResultPagination

    def get_queryset(self):

        job = ExtractionJob.objects.get(
            pk=self.kwargs["job_id"]
        )

        return job.records.all()
class CancelJobView(APIView):

    def post(self, request, job_id):

        try:
            job = ExtractionJob.objects.get(
                pk=job_id
            )
        except ExtractionJob.DoesNotExist:
            return Response(
                {
                    "detail": "Job not found"
                },
                status=404
            )

        if job.status in [
            JobStatus.COMPLETED,
            JobStatus.FAILED,
        ]:
            return Response(
                {
                    "detail":
                    "Job cannot be cancelled"
                },
                status=409
            )

        job.status = JobStatus.CANCELLED
        job.save()

        return Response({
            "message": "cancelled"
        })
class RemoveJobView(APIView):

    def delete(self, request, job_id):

        try:
            job = ExtractionJob.objects.get(
                pk=job_id
            )
        except ExtractionJob.DoesNotExist:
            return Response(
                {
                    "detail": "Job not found"
                },
                status=404
            )

        job.delete()

        return Response(
            status=204
        )
class JobListView(ListAPIView):

    serializer_class = JobSerializer

    def get_queryset(self):
        return ExtractionJob.objects.all()
class StatisticsView(APIView):

    def get(self, request):

        total = ExtractionJob.objects.count()

        completed = ExtractionJob.objects.filter(
            status=JobStatus.COMPLETED
        ).count()

        failed = ExtractionJob.objects.filter(
            status=JobStatus.FAILED
        ).count()

        return Response({
            "total_jobs": total,
            "completed_jobs": completed,
            "failed_jobs": failed
        })

    
