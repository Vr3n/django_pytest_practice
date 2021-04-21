import pytest

from django.contrib.auth.models import User

from ..models import Product, Category


# Testing the User Model.

@pytest.mark.django_db
def test_create_user(new_user1):
    count = User.objects.all().count()
    assert count >= 1


def test_staff_user(new_user1):
    print(new_user1.is_staff)
    assert new_user1.is_staff == True


# Testing the Product model.

@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ('NewTitle', 1, "NewDescription", "slug", "4.99", "3.99", True),
        ('NewTitle', 1, "NewDescription", "slug", "5.5", "3.99", True),
    ]
)
def test_product_instance(db, product_factory, title, category, description, slug, regular_price, discount_price, validity):
    test = product_factory(
        title=title,
        category_id=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price,
    )

    count = Product.objects.count()
    assert count == validity


# Testing the Category model.

@pytest.mark.django_db
def test_category_create(new_category):
    count = Category.objects.count()
    assert count == 1
