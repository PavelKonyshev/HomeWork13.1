
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
        self.__goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


    @property
    def goods(self):
        """Получение приватного атрибута __goods"""
        return self.__goods

    def add_goods(self, product):
        """Добавление данных с приватного атрибута __goods"""
        self.__goods.append(product)

    @property
    def __str__(self):
        """Получение имени, цены и остатка"""
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        self.count_of_products = len(self.__goods)
        return f'{self.name}, количество продуктов: {self.count_of_products} шт.'