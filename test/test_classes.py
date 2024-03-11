import pytest
from src.class_category import Category
from src.class_product import Product



@pytest.fixture
def class_category():
    return Category('Средства личной гигиены',
                    'Для волос и не только',
                    {
                        "name": "Head & Shoulders",
                        "description": "Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл",
                        "price": 585.91,
                        "quantity": 6
                    })
def test_category_init(class_category):
    assert  class_category.name == 'Средства личной гигиены'
    assert  class_category.description == 'Для волос и не только'
    assert  class_category.goods == {
                        "name": "Head & Shoulders",
                        "description": "Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл",
                        "price": 585.91,
                        "quantity": 6
                    }
    assert class_category.total_numbers_of_category == 1
    assert class_category.unique_goods == 1

@pytest.fixture
def class_product():
    return Product("Head & Shoulders", "Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл",
                   585.91, 6)

def test_product_init(class_product):
    assert class_product.name == 'Head & Shoulders'
    assert class_product.description == 'Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл'
    assert class_product.price == 585.91
    assert class_product.quantity == 6


def test_get_name(class_category):
    class_category.get_name()
    assert class_category.get_name() == 'Средства личной гигиены'


def test_get_description(class_category):
    class_category.get_description()
    assert class_category.get_description() == 'Для волос и не только'


@pytest.fixture
def class_products():
    return Product("Head & Shoulders", "Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл",
                   585.91, 6)


def test_products_init(class_product):
    assert class_product.name == 'Head & Shoulders'
    assert class_product.description == 'Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл'
    assert class_product.price == 585.91
    assert class_product.quantity == 6


def test_products_name(class_product):
    class_product.get_product_name()
    assert class_product.get_product_name() == 'Head & Shoulders'


def test_products_description(class_product):
    class_product.get_product_description()
    assert class_product.get_product_description() == 'Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл'

def test_products_quantity(class_product):
    class_product.get_product_quantity()
    assert class_product.get_product_quantity() != 5


