import factory
from faker import Faker

from django.contrib.auth.models import User
from ..models import Category, Product

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.name()
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "django"


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product

    title = "product_name"
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"
