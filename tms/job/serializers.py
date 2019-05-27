from django.shortcuts import get_object_or_404

from rest_framework import serializers

from . import models as m
from ..order.models import OrderProductDeliver
from ..order.serializers import (
    ShortOrderProductDeliverSerializer
)
from ..vehicle.serializers import ShortVehicleSerializer
from ..account.serializers import ShortStaffProfileSerializer
from ..road.serializers import RouteDataSerializer


class MissionSerializer(serializers.ModelSerializer):

    mission = ShortOrderProductDeliverSerializer()

    class Meta:
        model = m.Mission
        fields = (
            'loading_weight', 'unloading_weight', 'is_completed', 'mission'
        )


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Job
        fields = '__all__'

    def create(self, validated_data):
        mission_ids = self.context.get('mission_ids')
        mission_weights = self.context.get('mission_weights')
        job = m.Job.objects.create(**validated_data)
        for i, mission_id in enumerate(mission_ids):
            mission = get_object_or_404(OrderProductDeliver, pk=mission_id)
            m.Mission.objects.create(
                mission=mission,
                job=job,
                mission_weight=mission_weights[i]
            )
        return job


class JobDataSerializer(serializers.ModelSerializer):

    vehicle = ShortVehicleSerializer()
    driver = ShortStaffProfileSerializer()
    escort = ShortStaffProfileSerializer()
    route = RouteDataSerializer()
    missions = MissionSerializer(
        source='mission_set', many=True, read_only=True
    )

    class Meta:
        model = m.Job
        fields = (
            'id', 'vehicle', 'driver', 'escort', 'route', 'missions'
        )