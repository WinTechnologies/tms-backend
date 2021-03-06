from django.db import models

from . import managers
from ..core import constants as c
from ..core.models import TimeStampedModel, BasicContactModel
from ..hr.models import CustomerProfile


class Product(TimeStampedModel):
    """
    Product model
    """
    name = models.CharField(
        max_length=100,
        unique=True
    )

    level = models.PositiveIntegerField(
        default=3
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name


class BasicSetting(TimeStampedModel):
    """
    Basic setting modal
    """
    tax_rate = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    rapid_acceleration = models.PositiveIntegerField(
        default=0
    )

    rapid_deceleration = models.PositiveIntegerField(
        default=0
    )

    sharp_turn = models.PositiveIntegerField(
        default=0
    )

    over_speed = models.PositiveIntegerField(
        default=0
    )

    over_speed_duration = models.PositiveIntegerField(
        default=0
    )

    rotation_speed = models.PositiveIntegerField(
        default=0
    )

    driver_license_expires_notification_duration = models.PositiveIntegerField(
        default=0
    )

    driver_license_expires_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )

    driver_work_license_expires_notification_duration = models.PositiveIntegerField(
        default=0
    )

    driver_work_license_expires_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )

    vehicle_license_expires_notification_duration = models.PositiveIntegerField(
        default=0
    )

    vehicle_license_expires_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )

    vehicle_operation_permit_notification_duration = models.PositiveIntegerField(
        default=0
    )

    vehicle_operation_permit_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )

    vehicle_insurance_notification_duration = models.PositiveIntegerField(
        default=0
    )

    vehicle_insurance_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )

    trailer_usage_expires_notification_duration = models.PositiveIntegerField(
        default=0
    )

    trailer_usage_expires_notification_duration_unit = models.CharField(
        max_length=1,
        choices=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION,
        default=c.DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY
    )


class Station(BasicContactModel):
    """
    Station model, used as base class
    """
    station_type = models.PositiveIntegerField(
        choices=c.STATION_TYPE,
        default=c.STATION_TYPE_LOADING_STATION
    )

    longitude = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=10
    )

    latitude = models.DecimalField(
        default=0,
        max_digits=20,
        decimal_places=10
    )

    radius = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    products = models.ManyToManyField(
        Product
    )

    customers = models.ManyToManyField(
        CustomerProfile
    )

    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    working_time = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    working_time_measure_unit = models.CharField(
        max_length=1,
        choices=c.TIME_MEASURE_UNIT,
        default=c.TIME_MEASURE_UNIT_HOUR
    )

    average_time = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    average_time_measure_unit = models.CharField(
        max_length=1,
        choices=c.TIME_MEASURE_UNIT,
        default=c.TIME_MEASURE_UNIT_HOUR
    )

    price_vary_duration = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    price_vary_duration_unit = models.CharField(
        max_length=1,
        choices=c.PRICE_VARY_DURATION_UNIT,
        default=c.PRICE_VARY_DURATION_UNIT_MONTH
    )

    notification_message = models.TextField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    province = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    district = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    detail_address = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    objects = models.Manager()
    loadingstations = managers.LoadingStationManager()
    unloadingstations = managers.UnLoadingStationManager()
    qualitystations = managers.QualityStationManager()
    loadingqualitystations = managers.LoadingQualityStationManager()
    workstations = managers.WorkStationManager()
    oilstations = managers.OilStationManager()
    blackdots = managers.BlackDotManager()
    parkingstations = managers.ParkingStationManager()
    getoffstations = managers.GetoffStationManager()
    repairstations = managers.RepairStationManager()

    class Meta:
        ordering = ['station_type', '-updated']

    def __str__(self):
        return self.name


class TransportationDistance(TimeStampedModel):

    name = models.CharField(
        max_length=100
    )

    start_point = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='start_points'
    )

    end_point = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='end_points'
    )

    distance = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    average_time = models.DecimalField(
        default=1,
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        null=True,
        blank=True
    )


class OtherCostType(models.Model):

    name = models.CharField(
        max_length=100
    )


class TicketType(models.Model):

    name = models.CharField(
        max_length=100
    )
