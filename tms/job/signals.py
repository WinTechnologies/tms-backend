import json
from django.dispatch import receiver
from django.db.models.signals import post_save

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from . import models as m
from ..account.models import User
from ..core import constants as c
from ..notification.models import Notification
from ..notification.serializers import NotificationSerializer


channel_layer = get_channel_layer()


@receiver(post_save, sender=m.Job)
def notify_driver_of_new_job(sender, instance, **kwargs):
    message = "A new mission is assigned to you."\
        "Please use {}".format(instance.vehicle)

    notification = Notification.objects.create(
        user=instance.driver,
        message=message,
        msg_type=c.DRIVER_NOTIFICATION_TYPE_JOB
    )

    if instance.driver.channel_name is not None:
        async_to_sync(channel_layer.send)(
            instance.driver.channel_name,
            {
                'type': 'notify',
                'data': json.dumps(NotificationSerializer(notification).data)
            }
        )


@receiver(post_save, sender=m.ParkingRequest)
def notify_staff_of_parking_request(sender, instance, **kwargs):
    message = "{} created {} parking request."\
        "Please approve it".format(instance.driver, instance.vehicle)

    admin = User.objects.get(role=c.USER_ROLE_ADMIN)[0]
    notification = Notification.objects.create(
        user=admin,
        message=message,
        msg_type=c.DRIVER_NOTIFICATION_TYPE_JOB
    )

    if admin.channel_name is not None:
        async_to_sync(channel_layer.send)(
            admin.channel_name,
            {
                'type': 'notify',
                'data': json.dumps(NotificationSerializer(notification).data)
            }
        )


@receiver(post_save, sender=m.DriverChangeRequest)
def notify_staff_of_driver_change_request(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=m.DriverChangeRequest)
def notify_staff_of_escort_change_request(sender, instance, **kwargs):
    pass