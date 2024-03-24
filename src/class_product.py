from abc import ABC, abstractmethod

class AbsctactProduct(ABC):
    @abstractmethod
    def launch_product(cls, new_product):
        """
        класс метод добавления новых товаров
        """
class MixinLog:
    """
    Класс миксин для вывода repr
    """
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        list_attr = []
        for i in self.__dict__.items():
            list_attr.append(i[1])
            return f'Создание нового экземпляра родукта - {self.__class__.__name__}{tuple(list_attr)}'
class Product(MixinLog, AbsctactProduct):
    name: str
    description: str
    price: float
    quantity: int
    count_product = 0
    def __init__(self, name, description, price, quantity):
        """Инициализация класса продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.count_product += 1
        super().__init__()

    @classmethod
    def launch_product(cls, new_product):
        return cls(**new_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        elif new_price < self.__price:
            user_answer = input("Цена понизилась. Установить эту цену? (y - да, n - нет)")
            if user_answer == "y":
                self.__price = new_price
            else:
                print("Цена осталась прежней")
                self.__price = new_price

    @property
    def new_price(self):
        return self.new_price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'


    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        name = product_data["name"]
        description = product_data["descriptoin"]
        price = product_data["price"]
        quantity = product_data["quantity_in_stock"]
        if list_of_products:
            for product in list_of_products:
                if product_data == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product
        new_product = cls(name, description, price, quantity)
        return new_product

    def __add__(self, other):
        if type(self) == type(other):
            results = (self.__price * self.quantity) + (other.__price * other.quantity)
            return results
        else:
            raise TypeError('Можно складывать только экземпляры одного и того же класса!')

    def __str__(self):
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

class SmartPhone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.perfomace = performance
        self.model = model
        self.memory = memory
        self.color = color


    def __str__(self):
        return super().__str__() + f", Модель: {self.model}, Цвет: {self.color}, Память: {self.memory}GB"

class LawGrass(Product):
    def __init__(self, name, description, price, quantity, manufacturer, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination_time = germination_time
        self.color = color

    def __str__(self):
        return super().__str__() + (f", Страна: {self.manufacturer}, "
                                    f"Время прорастания: {self.germination_time} дней, Цвет: {self.color}")

if __name__ == '__main__':
    # Создание словаря для дальнейшего добавления в экземпляры класса
    new_product_3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }

    product_3 = Product.launch_product(new_product_3)  # Добавление нового продукта
    print(product_3)  # Вывод добавленного словаря

    product_1 = Product('Samsung', 'smth', 90_000, 2)
    print(product_1)
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product

    lawngrass_1 = LawGrass("трава", "газонная", 100, 3, "Russia", "5 лет", "зеленая")

    print(f'Метод add для 2х экземпляров класса Product: {product_1 + product_2}')

