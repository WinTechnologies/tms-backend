from collections import OrderedDict
from django.db import models

from jsonfield import JSONField
from ..core import constants as c
from ..core.models import TimeStampedModel
from ..account.models import User
from ..vehicle.models import Vehicle
from . import managers


class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    msg_type = models.PositiveIntegerField(
        choices=c.NOTIFICATION_TYPE,
        default=c.DRIVER_NOTIFICATION_NEW_JOB
    )

    message = JSONField(load_kwargs={'object_pairs_hook': OrderedDict})

    is_read = models.BooleanField(
        default=False
    )

    sent_on = models.DateTimeField(
        auto_now_add=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    objects = models.Manager()
    unreads = managers.UnreadNotificationManager()
    reads = managers.ReadNotificationManager()
    availables = managers.AvailableNotificationManager()
    deletes = managers.DeletedNotificationManager()

    class Meta:
        ordering = (
            'is_read', '-sent_on'
        )

    def __str__(self):
        return 'Meessage to {}'.format(
            self.user.username
        )


class Event(models.Model):

    event_type = models.PositiveIntegerField(
        default=c.EVENT_TYPE_DRIVER_LICENSE_EXPIRED,
        choices=c.EVENT_TYPE
    )

    expires_on = models.DateField()

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_head = models.BooleanField(
        default=False
    )

    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_processed = models.BooleanField(
        default=False
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    objects = models.Manager()
    processed_events = managers.ProcessedEventManager()
    pending_events = managers.PendingEventManager()

    class Meta:
        ordering = (
            '-created_on',
            'is_processed'
        )


class G7MQTTEvent(TimeStampedModel):

    event_type = models.PositiveIntegerField(
        default=c.MQTT_EVENT_STOP,
        choices=c.MQTT_EVENT_TYPE
    )

    push_time = models.DateTimeField(
        null=True,
        blank=True
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events_as_driver',
    )

    escort = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events_as_escort',
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True
    )

    seconds = models.PositiveIntegerField(
        default=0
    )

    start_lng = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=10
    )

    start_lat = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=10
    )

    end_lng = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=10
    )

    end_lat = models.DecimalField(
        null=True,
        blank=True,
        max_digits=20,
        decimal_places=10
    )
