import pytest

from src.classes import Category, Product


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
    assert  class_category.unique_goods == 1

@pytest.fixture
def class_product():
    return Product("Head & Shoulders", "Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл",
                   585.91, 6)

def test_product_init(class_product):
    assert class_product.name == 'Head & Shoulders'
    assert class_product.description == 'Head&Shoulders 2в1 Основной уход для нормальных волос, 300 мл'
    assert class_product.price == 585.91
    assert class_product.quantity_in_stock == 6