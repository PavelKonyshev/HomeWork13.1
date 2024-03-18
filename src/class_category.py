from src.class_product import Product
from abc import ABC, abstractmethod

class AbstectCategory(ABC):
    @abstractmethod
    def __init__(self):
        """
        абстрактный метод инициализация
        """


class Category(AbstectCategory):
    """Создание класса категории"""
    name = str
    description: str
    goods: list
    total_numbers_of_category = 0
    unique_goods = 0


    def __init__(self, name, description):
        """Инициализация класса категории"""
        self.name = name
        self.description = description
        self.__goods = []

        Category.total_numbers_of_category += 1 #Счетчик общего количества категорий


    @property
    def goods(self):
        """Получение приватного атрибута __goods"""
        return self.__goods

    def add_goods(self, good):
        """
        Метод добавления товара в список и считает итоговое количество всех продуктов
        """
        if isinstance(good, Product):
            for item in self.__goods:
                if item[0] == good.name:
                    item[3] += good.quantity
                    break
            else:
                self.__goods.append([good.name, good.description, good.price, good.quantity])
                Category.unique_goods += 1
        else:
            return f'Нельзя добавить объект отличный от класса Product или его наследников'


    @property
    def counting_goods(self):
        count = 0
        for i in self.__goods:
            count += i[3]
        return count
    def __repr__(self):
        """
        отоброжение экземляра категории
        """
        return f'{self.name}, {self.description}, {self.__goods}'

    @property
    def get_format(self):
        """
        геттер для вывода формата
        """
        result = ''
        for good in self.__goods:
            result += f'{good[0]}, {good[2]} руб. Остаток: {good[3]} шт. \n'
        return result

    def __len__(self):
        """
        Вывод количества продуктов на складе
        """
        return len(self.__goods)

    def __str__(self):
        """Получение имени, цены и остатка"""
        return f'Название категории: {self.name}, количество продуктов: {self.__len__()} шт.'



if __name__ == '__main__':
    category_1 = Category('Телефоны', 'мобильные телефоны')  # Экземпляр класса Category
    product_1 = Product('Samsung', 'smth', 90_000, 2)  # Экземпляр класса Product
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product
    print(category_1.goods)

    category_1.add_goods(product_1)  # Добавление продукта в приватный список товаров
    print(category_1.goods)
    category_1.add_goods(product_2)  # Добавление продукта в приватный список товаров
    print(category_1.goods)

    product_3 = Product('iPhone', 'smth', 100_000, 34)
    category_1.add_goods(product_3)  # Добавление продукта в приватный список товаров если такой продукт существует
    print(category_1.goods)  # Отображение приватного списка товаров

    print(f'Уникальных продуктов: {category_1.total_numbers_of_category}')  # Количество уникальных товаров в приватном списке
    print(category_1.__str__)  # Получение перечня товаров определенным форматом
    print(str(category_1))  # Отображение строкового представления

    print(f'Вывод  общего количества продуктов категории: {category_1.total_numbers_of_category}')

    class Something:
        pass

    something = Something()
    category_1.add_goods(something)