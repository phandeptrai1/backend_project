from rest_framework import serializers

from .models import ExtractionJob
from .models import ExtractedRecord


class StartScanSerializer(serializers.Serializer):
    api_token = serializers.CharField()


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtractionJob
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtractedRecord
        fields = (
            "id",
            "external_id",
            "email",
            "first_name",
            "last_name",
        )
