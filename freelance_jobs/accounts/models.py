from django.db import models
from django.contrib.auth.models import User
import uuid


class UserJobs(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    job_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name='UUID',
        unique=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    category = models.CharField(
        max_length=255,
        verbose_name='Category'
    )
    description = models.TextField(
        verbose_name='Description',
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Location',
    )
    payment_type = models.CharField(
        max_length=16,
        verbose_name='Payment type',
    )
    payment = models.PositiveIntegerField(
        verbose_name='Payment',
        default=0
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time added'
    )

    def __str__(self):
        return f"Job for {self.user.username}"

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
