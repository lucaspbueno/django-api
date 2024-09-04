
import uuid
from django.db import models
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value <= 0:
        raise ValidationError('O valor deve ser maior que zero.')


class Equipment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nm_equipment = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    tp_equipment = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    nm_manufacturer = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    nm_model = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    nr_serial = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    dt_purchase = models.DateTimeField(
        blank=True,
        null=True
    )
    vlr_purchase = models.FloatField(
        validators=[validate_positive],
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # vl_amount = models.IntegerField()

    class Meta:
        db_table = 'equipment'
        verbose_name_plural = 'equipment'

    def __str__(self):
        return self.nm_Equipment
