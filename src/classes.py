class Category:
    """Создание класса категории"""
    name = str
    description: str
    goods: list

class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int