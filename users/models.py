from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import AgeCheckValidator, EmailCheckValidator


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"

    ROLES = [
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN)
    ]

    role = models.CharField(max_length=100, choices=ROLES, default=USER)
    age = models.PositiveSmallIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, validators=[AgeCheckValidator])
    email = models.EmailField(unique=True, null=True, validators=[EmailCheckValidator])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
