from django.db import models
from django.contrib.postgres.fields import ArrayField

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

    code = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=10,
        choices=c.PRODUCT_CATEGORY,
        default=c.PRODUCT_CATEGORY_GASOLINE
    )

    price = models.DecimalField(
        max_digits=c.PRICE_MAX_DIGITS,
        decimal_places=c.PRICE_DECIMAL_PLACES
    )

    unit_weight = models.PositiveIntegerField(
        default=1
    )

    weight_measure_unit = models.CharField(
        max_length=1,
        choices=c.PRODUCT_WEIGHT_MEASURE_UNIT,
        default=c.PRODUCT_WEIGHT_MEASURE_UNIT_TON
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name


class Station(BasicContactModel):
    """
    Station model, used as base class
    """
    station_type = models.CharField(
        max_length=1,
        choices=c.STATION_TYPE,
    )

    longitude = models.FloatField()

    latitude = models.FloatField()

    radius = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    products = models.ManyToManyField(
        Product
    )

    customer = models.ForeignKey(
        CustomerProfile,
        on_delete=models.SET_NULL,
        null=True
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True
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

    objects = models.Manager()
    loadingstations = managers.LoadingStationManager()
    unloadingstations = managers.UnLoadingStationManager()
    qualitystations = managers.QualityStationManager()
    loadingqualitystations = managers.LoadingQualityStationManager()
    workstations = managers.WorkStationManager()
    oilstations = managers.OilStationManager()
    blackdots = managers.BlackDotManager()

    class Meta:
        ordering = ['station_type', '-updated']

    def __str__(self):
        return self.name


class Route(TimeStampedModel):

    name = models.CharField(
        max_length=100,
    )

    # current map api allow only 16 waypoints
    path = ArrayField(
        models.PositiveIntegerField(),
        size=18
    )

    policy = models.PositiveIntegerField(
        choices=c.ROUTE_PLANNING_POLICY,
        default=c.ROUTE_PLANNING_POLICY_LEAST_TIME
    )

    distance = models.PositiveIntegerField()

    @property
    def loading_station(self):
        try:
            return Station.loadingstations.get(pk=self.path[0])
        except Station.DoesNotExist:
            return None

    @property
    def unloading_stations(self):
        stations = Station.unloadingstations.filter(id__in=self.path)
        stations = dict([(station.id, station) for station in stations])
        unloading_stations = []
        for id in self.path:
            if id in stations:
                unloading_stations.append(stations[id])

        return unloading_stations

    @property
    def stations(self):
        points = Station.workstations.filter(id__in=self.path)
        points = dict([(point.id, point) for point in points])
        return [points[id] for id in self.path]

    @property
    def stations_count(self):
        return Station.workstations.filter(id__in=self.path).count()

    def __str__(self):
        return self.name
