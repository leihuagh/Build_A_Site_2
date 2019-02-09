from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampModel


class Question(TimeStampModel):
    title = models.CharField(max_length=225)
    status = models.CharField(max_length=10, default="inactivate")
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

