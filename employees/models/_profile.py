from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampModel


class Profile(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ('-salary', )

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    def user_username(self):
        return self.user.username

    def user_email(self):
        return self.user.email
