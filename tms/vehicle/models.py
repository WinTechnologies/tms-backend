from django.db import models
from django.contrib.postgres.fields import ArrayField

from . import managers
from ..core import constants as c

# models
from ..core.models import TimeStampedModel
from ..account.models import User
from ..info.models import Station


class Vehicle(TimeStampedModel):
    """
    Vehicle model
    """
    department = models.PositiveIntegerField(
        choices=c.VEHICLE_DEPARTMENT_TYPE,
        default=c.VEHICLE_DEPARTMENT_TYPE_OIL
    )

    # Basic Information
    model = models.CharField(
        max_length=1,
        choices=c.VEHICLE_MODEL_TYPE,
        default=c.VEHICLE_MODEL_TYPE_TRUCK
    )

    plate_num = models.CharField(
        max_length=100,
        unique=True
    )

    identifier_code = models.CharField(
        max_length=100
    )

    brand = models.CharField(
        max_length=1,
        choices=c.VEHICLE_BRAND,
        default=c.VEHICLE_BRAND_TONGHUA
    )

    use_for = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    total_load = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    actual_load = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    model_2 = models.CharField(
        max_length=1,
        choices=c.VEHICLE_MODEL_TYPE,
        default=c.VEHICLE_MODEL_TYPE_TRUCK
    )

    plate_num_2 = models.CharField(
        max_length=100,
        unique=True
    )

    identifier_code_2 = models.CharField(
        max_length=100
    )

    brand_2 = models.CharField(
        max_length=1,
        choices=c.VEHICLE_BRAND,
        default=c.VEHICLE_BRAND_TONGHUA
    )

    use_for_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    total_load_2 = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    actual_load_2 = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    tank_volume = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    affiliation_unit = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    use_started_on = models.DateField(
        null=True,
        blank=True
    )

    use_expires_on = models.DateField(
        null=True,
        blank=True
    )

    service_area = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    obtain_method = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    attribute = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # Identity Information
    license_type = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_authority = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_registered_on = models.DateField(
        null=True,
        blank=True
    )

    license_active_on = models.DateField(
        null=True,
        blank=True
    )

    license_expires_on = models.DateField(
        null=True,
        blank=True
    )

    operation_permit_active_on = models.DateField(
        null=True,
        blank=True
    )

    operation_permit_expires_on = models.DateField(
        null=True,
        blank=True
    )

    insurance_active_on = models.DateField(
        null=True,
        blank=True
    )

    insurance_expires_on = models.DateField(
        null=True,
        blank=True
    )

    license_type_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_id_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_authority_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    license_registered_on_2 = models.DateField(
        null=True,
        blank=True
    )

    license_active_on_2 = models.DateField(
        null=True,
        blank=True
    )

    license_expires_on_2 = models.DateField(
        null=True,
        blank=True
    )

    operation_permit_active_on_2 = models.DateField(
        null=True,
        blank=True
    )

    operation_permit_expires_on_2 = models.DateField(
        null=True,
        blank=True
    )

    insurance_active_on_2 = models.DateField(
        null=True,
        blank=True
    )

    insurance_expires_on_2 = models.DateField(
        null=True,
        blank=True
    )

    # Position Information
    branches = ArrayField(
        models.DecimalField(
            max_digits=10,
            decimal_places=2
        )
    )

    # Hardware Information
    engine_model = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    engine_power = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    transmission_model = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    engine_displacement = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tire_rules = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tank_material = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    is_gps_installed = models.BooleanField(
        default=False
    )

    is_gps_working = models.BooleanField(
        default=False
    )

    with_pump = models.BooleanField(
        default=False
    )

    main_car_size = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    main_car_color = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    trailer_car_size = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    trailer_car_color = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    status = models.PositiveIntegerField(
        choices=c.VEHICLE_STATUS,
        default=c.VEHICLE_STATUS_AVAILABLE
    )

    @property
    def branch_count(self):
        return len(self.branches)

    # @property
    # def bound_driver(self):
    #     bind = VehicleWorkerBind.objects.filter(
    #         vehicle=self
    #     ).first()
    #     if bind is not None and bind.get_off is None:
    #         driver = bind.driver
    #     else:
    #         driver = 'No driver'

    #     return driver

    @property
    def next_job_customer(self):
        next_job = self.jobs.filter(progress=c.JOB_PROGRESS_NOT_STARTED).first()
        customer_name = ''
        if next_job:
            next_order = next_job.order.first()
            if next_order:
                customer = next_order.customer.first()
                customer_name = customer.user.username
        return customer_name

    objects = models.Manager()
    inworks = managers.UnderWheelVehicleManager()
    availables = managers.AvailableVehicleManager()
    repairs = managers.RepairVehicleManager()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.plate_num


class FuelConsumption(TimeStampedModel):

    vehicle_type = models.CharField(
        max_length=100
    )

    high_way = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    normal_way = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        null=True,
        blank=True
    )


class VehicleMaintenanceHistory(TimeStampedModel):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    category = models.PositiveIntegerField(
        choices=c.VEHICLE_MAINTENANCE_CATEGORY,
        default=c.VEHICLE_MAINTENANCE_CATEGORY_0
    )

    maintenance_date = models.DateField()

    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    station = models.ForeignKey(
        Station,
        on_delete=models.SET_NULL,
        null=True
    )

    total_cost = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    mileage = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    accessories_fee = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    work_fee = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    ticket_type = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tax_rate = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        null=True,
        blank=True
    )


class VehicleCheckItem(TimeStampedModel):

    name = models.CharField(
        max_length=100
    )

    is_before_driving_item = models.BooleanField(
        default=False
    )

    is_driving_item = models.BooleanField(
        default=False
    )

    is_after_driving_item = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    objects = models.Manager()
    before_driving_check_items = managers.BeforeDrivingCheckItemsManager()
    driving_check_items = managers.DrivingCheckItemsManager()
    after_driving_check_items = managers.AfterDrivingCheckItemsManager()
    published_before_driving_check_items = managers.PublishedBeforeDrivingCheckItemsManager()
    published_driving_check_items = managers.PublishedDrivingCheckItemsManager()
    published_after_driving_check_items = managers.PublishedAfterDrivingCheckItemsManager()


class VehicleCheckHistory(TimeStampedModel):

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_vehicle_checks'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    before_driving_problems = models.PositiveIntegerField(
        default=0
    )

    before_driving_description = models.TextField(
        null=True, blank=True
    )

    before_driving_solution = models.TextField(
        null=True,
        blank=True
    )

    before_driving_checked_time = models.DateTimeField(
        null=True, blank=True
    )

    driving_problems = models.PositiveIntegerField(
        default=0
    )

    driving_description = models.TextField(
        null=True, blank=True
    )

    driving_solution = models.TextField(
        null=True,
        blank=True
    )

    driving_checked_time = models.DateTimeField(
        null=True, blank=True
    )

    after_driving_problems = models.PositiveIntegerField(
        default=0
    )

    after_driving_description = models.TextField(
        null=True, blank=True
    )

    after_driving_solution = models.TextField(
        null=True,
        blank=True
    )

    after_driving_checked_time = models.DateTimeField(
        null=True, blank=True
    )

    before_driving_checked_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleBeforeDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item'),
        related_name='befores'
    )

    driving_checked_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item'),
        related_name='drivings'
    )

    after_driving_checked_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleAfterDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item'),
        related_name='afters'
    )

    class Meta:
        ordering = ['-updated']


class VehicleCheckDocument(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleCheckHistory,
        on_delete=models.CASCADE,
        related_name='images'
    )

    document_type = models.CharField(
        max_length=1,
        choices=c.VEHICLE_CHECK_TYPE,
        default=c.VEHICLE_CHECK_TYPE_BEFORE_DRIVING
    )

    document = models.ImageField()


class VehicleBeforeDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )


class VehicleDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )


class VehicleAfterDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )


class VehicleWorkerBind(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_vehicle_bind'
    )

    worker_type = models.CharField(
        max_length=1,
        choices=c.WORKER_TYPE,
        default=c.WORKER_TYPE_DRIVER
    )

    get_on = models.DateTimeField(
        auto_now_add=True
    )

    get_off = models.DateTimeField(
        null=True,
        blank=True
    )

    get_off_station = models.ForeignKey(
        Station,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    objects = models.Manager()
    driverbinds = managers.VehicleDriverBindManager()
    escortbinds = managers.VehicleEscortBindManager()

    class Meta:
        ordering = ['-get_on', 'vehicle']


class VehicleTire(TimeStampedModel):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    position = models.CharField(
        max_length=100
    )

    @property
    def current_tire(self):
        return self.history.first()

    class Meta:
        unique_together = [
            'vehicle', 'position'
        ]


class TireManagementHistory(TimeStampedModel):

    vehicle_tire = models.ForeignKey(
        VehicleTire,
        on_delete=models.CASCADE,
        related_name='history'
    )

    installed_on = models.DateTimeField()

    mileage = models.DecimalField(
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2
    )

    mileage_limit = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    tire_type = models.CharField(
        max_length=100
    )

    tread_depth = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    manufacturer = models.CharField(
        max_length=100
    )

    contact_number = models.CharField(
        max_length=100
    )

    tire_mileage = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    vehicle_mileage = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    @property
    def current_tread_depth(self):
        return self.history.first()

    class Meta:
        ordering = [
            '-installed_on',
        ]


class TireTreadDepthCheckHistory(TimeStampedModel):

    tire = models.ForeignKey(
        TireManagementHistory,
        on_delete=models.CASCADE,
        related_name='history'
    )

    mileage = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    pressure = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    tread_depth = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    symptom = models.TextField(
        null=True,
        blank=True
    )

    checked_on = models.DateTimeField()

    @property
    def before_tread_depth(self):
        before_thread_depth = self.tire.history.filter(checked_on__lt=self.checked_on).first()
        if before_thread_depth is not None:
            return before_thread_depth.tread_depth
        else:
            return self.tire.tread_depth

    class Meta:
        ordering = (
            '-checked_on',
        )


class VehicleDriverEscortBind(models.Model):

    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='bind'
    )

    driver = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="vehicles_as_driver"
    )

    escort = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="vehicles_as_escort"
    )


class VehicleViolation(models.Model):

    # vehicle = models.ForeignKey(
    #     Vehicle,
    #     on_delete=models.CASCADE
    # )

    # driver = models.ForeignKey(
    #     User,
    #     on_delete=models.SET_NULL,
    #     null=True
    # )

    vehicle = models.CharField(
        max_length=100
    )

    driver = models.CharField(
        max_length=100
    )

    address = models.CharField(
        max_length=500
    )

    fine = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2
    )

    deduction_score = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    # status = models.PositiveIntegerField(
    #     default=c.VEHICLE_VIOLATION_STATUS_PENDING,
    #     choices=c.VEHICLE_VIOLATION_STATUS
    # )

    description = models.TextField(
        null=True,
        blank=True
    )

    violates_on = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # violates_on = models.DateTimeField(
    #     null=True,
    #     blank=True
    # )
