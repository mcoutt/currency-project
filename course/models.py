from django.db import models
import uuid


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    currency_value = models.CharField(max_length=50, null=True, blank=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = "Course's"

    def __str__(self):
        return f"{self.currency_name}/{self.currency_value}"
