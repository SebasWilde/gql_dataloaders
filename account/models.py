from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model
    """

    best_friend = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )
    best_friends = models.ManyToManyField('self', blank=True)
