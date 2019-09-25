from django.db import models
import uuid
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule


# schedule = IntervalSchedule.objects.create(every=5, period=IntervalSchedule.SECONDS)
# task = PeriodicTask.objects.create(interval=schedule, name='Save Currency info',
#                                    task='currency.save_currency_data',
#                                    args=json.dumps([66]))


class Currency(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True, default=None)
    code = models.CharField(max_length=50, null=True, blank=True, default=None)
    statuses = models.CharField(max_length=50, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = "Currency's"

    def __str__(self):
        return f"Name: {self.name}; Code: {self.code}"


class Course(models.Model):
    # id = models.AutoField(primary_key=True)
    currency_base = models.CharField(max_length=50, null=True, blank=True, default=None)
    # currency_target = models.CharField(max_length=50, null=True, blank=True, default=None)
    currency_target = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True, default=None)
    currency_value = models.CharField(max_length=50, null=True, blank=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = "Course's"

    def __str__(self):
        return f"{self.currency_base}/{self.currency_value}"
