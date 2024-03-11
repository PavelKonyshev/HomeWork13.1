import json
import os
from src import class_category
from src import class_product


def load_data():
    """Загружает даннные из json файла"""
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join("products.json")
    with open(PATH, encoding='UTF-8') as read_data:
        data = json.load(read_data)
        return data


def convert_data(categories):
    """Получение списков с категориями и товарами"""
    convert_categories = []
    for category in categories:
        convert_products = []
        for product in category["products"]:
            current_product = (class_product.Product(product["name"],
                                              product["description"],
                                              product["price"],
                                              product["quantity"]))
            convert_products.append(current_product)
        current_category = class_category.Category(category["name"],
                                            category["description"],
                                            convert_products)
        convert_categories.append(current_category)
    return convert_categories

for category in convert_data(load_data()):
    print(category)
    for product in category.goods():
        print(product)
        new_price = float(input("Введите новую цену"))
        product.price = new_price
        print(product)
