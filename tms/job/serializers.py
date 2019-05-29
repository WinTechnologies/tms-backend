from django.shortcuts import get_object_or_404

from rest_framework import serializers

from . import models as m
from ..order.models import OrderProductDeliver
from ..order.serializers import (
    ShortOrderProductDeliverSerializer, ShortStationSerializer,
)
from ..vehicle.serializers import MainVehicleSerializer
from ..account.serializers import ShortStaffProfileSerializer
from ..road.serializers import RouteDataSerializer


class MissionSerializer(serializers.ModelSerializer):

    mission = ShortOrderProductDeliverSerializer()

    class Meta:
        model = m.Mission
        fields = (
            'mission_weight', 'loading_weight', 'unloading_weight',
            'arrived_time_at_station', 'started_unloading_on',
            'finished_unloading_on', 'departure_time_at_station',
            'is_completed', 'mission'
        )


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Job
        fields = '__all__'

    def create(self, validated_data):
        mission_ids = self.context.get('mission_ids')
        mission_weights = self.context.get('mission_weights')
        job = m.Job.objects.create(**validated_data)
        stations = job.route.stations[2:]

        for i, mission_id in enumerate(mission_ids):
            mission = get_object_or_404(OrderProductDeliver, pk=mission_id)
            m.Mission.objects.create(
                mission=mission,
                job=job,
                step=stations.index(mission.unloading_station),
                mission_weight=mission_weights[i]
            )
        return job


class JobDataSerializer(serializers.ModelSerializer):

    vehicle = MainVehicleSerializer()
    driver = ShortStaffProfileSerializer()
    escort = ShortStaffProfileSerializer()
    route = RouteDataSerializer()
    missions = MissionSerializer(
        source='mission_set', many=True, read_only=True
    )
    stations = ShortStationSerializer(
        source='route.stations', many=True, read_only=True
    )

    progress_msg = serializers.CharField(source='get_progress_display')
    mission_count = serializers.SerializerMethodField()

    class Meta:
        model = m.Job
        fields = (
            'id', 'vehicle', 'driver', 'escort', 'stations',
            'route', 'missions', 'progress', 'progress_msg' 'total_weight',
            'start_due_time', 'finish_due_time', 'mission_count'
        )

    def get_mission_count(self, obj):
        return obj.missions.all().count()


class JobProgressSerializer(serializers.ModelSerializer):

    progress_msg = serializers.CharField(source='get_progress_display')

    class Meta:
        model = m.Job
        fields = (
            'id', 'progress', 'progress_msg'
        )


class JobBillDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.JobBillDocument
        fields = (
            'id', 'job', 'document', 'category'
        )


class DriverNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.DriverNotification
        fields = (
            'message', 'sent', 'is_read'
        )
