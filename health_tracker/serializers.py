from rest_framework.response import Response
from rest_framework import serializers, viewsets

from django.shortcuts import get_object_or_404

from health_records.models import HealthProfile, HealthRecord, PhysActivity, EatingInfo


class PhysicalActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = PhysActivity
        fields = '__all__'


class EatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = EatingInfo
        fields = '__all__'


class HealthRecordSerializer(serializers.ModelSerializer):
    physical_activity = PhysicalActivitySerializer(many=True)
    eating_info = EatingSerializer(many=True)

    class Meta:
        model = HealthRecord
        fields = ('activity_date', 'date_created', 'date_modified', 'weight', 'physical_activity', 'eating_info', )


# Serializers define the API representation.
class HealthProfileSerializer(serializers.ModelSerializer):
    records = HealthRecordSerializer(many=True)

    class Meta:
        model = HealthProfile
        fields = ('height', 'pk', 'records',)


class HealthProfileViewSet(viewsets.ModelViewSet):
    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer

    def retrieve(self, request, pk=None):
        queryset = HealthProfile.objects.all()
        profile = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(profile, context={'request': request})
        return Response(serializer.data)
