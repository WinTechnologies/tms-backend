from django.dispatch import receiver
from django.db.models.signals import post_save

from ..core import constants as c
# models
from . import models as m
from .tasks import calculate_job_report


@receiver(post_save, sender=m.Job)
def updated_job(sender, instance, created, **kwargs):

    if instance.progress == c.JOB_PROGRESS_COMPLETE:
        calculate_job_report.apply_async(
            args=[{
                'job': instance.id,
                'vehicle': instance.vehicle.id,
                'driver': instance.driver.id,
                'escort': instance.escort.id
            }]
        )
