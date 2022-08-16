from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from users.models import User


class Categorie(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=2000, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='logos/')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ads)
