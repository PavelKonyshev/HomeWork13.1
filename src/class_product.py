class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация класса продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_quantity(self):
        return self.quantity

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
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'