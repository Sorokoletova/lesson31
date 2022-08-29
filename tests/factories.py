import factory.django

from users.models import User
from ads.models import Ads, Categorie


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")


class CategorieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categorie

    slug = factory.Faker("word")
    name = factory.Faker("word")


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    category = factory.SubFactory(CategorieFactory)
    author = factory.SubFactory(UserFactory)
