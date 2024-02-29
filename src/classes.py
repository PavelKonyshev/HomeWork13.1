class Category:
    """Создание класса категории"""
    name = str
    description: str
    goods: list
    total_numbers_of_category = 0
    unique_goods = 0


    def __init__(self, name, description, goods):
        """Инициализация класса категории"""
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        """Инициализация класса продукт"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


