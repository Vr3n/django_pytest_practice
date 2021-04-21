import pytest

from pytest_factoryboy import register
from app1.tests.factories import UserFactory, CategoryFactory, ProductFactory

# access the fixture using: user_factory
register(UserFactory)

# access the fixture using: user_factory
register(CategoryFactory)

# access the fixture using: user_factory
register(ProductFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def new_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def new_product(db, product_factory):
    product = product_factory.create()
    return product
