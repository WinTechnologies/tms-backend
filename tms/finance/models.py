from django.db import models

from ..core import constants as c
from ..account.models import User
from ..hr.models import Department
from ..job.models import Job
from ..order.models import Order
from ..vehicle.models import Vehicle


class BaseCard(models.Model):

    issue_company = models.CharField(
        max_length=100
    )

    number = models.CharField(
        max_length=100,
        unique=True
    )

    key = models.CharField(
        max_length=100
    )

    last_charge_date = models.DateField(
        null=True,
        blank=True
    )

    balance = models.PositiveIntegerField(
        default=0
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        ordering = ['-last_charge_date']


class ETCCard(BaseCard):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )


class FuelCard(BaseCard):

    master = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        related_name='children'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True
    )


class OrderPayment(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=5,
        decimal_places=1
    )

    is_complete = models.BooleanField(
        default=False
    )


class BillDocument(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bills'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        related_name='bills',
        null=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=1
    )

    bill = models.ImageField()

    category = models.PositiveIntegerField(
        choices=c.BILL_TYPE,
        default=c.BILL_FROM_LOADING_STATION
    )

    def __str__(self):
        return '{} bill from {}'.format(
            self.get_category_display(),
            self.user
        )

    class Meta:
        ordering = [
            'category'
        ]
