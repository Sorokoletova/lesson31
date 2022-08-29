from pytest_factoryboy import register
from tests.factories import UserFactory, AdsFactory, CategorieFactory

pytest_plugins = "tests.fixtures"
register(UserFactory)
register(AdsFactory)
register(CategorieFactory)
