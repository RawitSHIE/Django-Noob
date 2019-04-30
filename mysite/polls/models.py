from django.contrib.auth.models import User
from django.db import models


class Dayoff(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField(max_length=100)
    SICK = 'sick'
    BUSINESS = 'business'
    TYPES = (
        (SICK, 'sick'),
        (BUSINESS, 'business')
    )
    type = models.CharField(max_length=10, choices=TYPES, default=SICK)
    date_start = models.DateField()
    date_end = models.DateField()
    PENDING = 'pending'
    DISAPPROVE = 'disapprove'
    APPROVE = 'approve'
    APPROVE_TYPE = (
        (PENDING, 'pending'),
        (DISAPPROVE, 'disapprove'),
        (APPROVE, 'approve')
    )

    approve_status = models.CharField(max_length=10,choices=APPROVE_TYPE, default=PENDING)