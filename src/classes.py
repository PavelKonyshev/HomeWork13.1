class Category:
    """Создание класса категории"""
    name = str
    description: str
    goods: str
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


    def get_goods(self):
        return self.__goods
    @property
    def goods(self):
        products_list = []
        for item in self.__goods:
            products_list.append(f'{item.name}, {item.price} руб. Остаток: {item.quantity_in_stock}')
        return products_list
    @goods.setter
    def good(self, product):
        if isinstance(product, Product):
            self.__goods.append(product)

    @property
    def products_list(self):
        return self.__goods

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        """Инициализация класса продукт"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_quantity_in_stock(self):
        return self.quantity_in_stock

    @property
    def get_product_price(self):
        return self.__price

    @get_product_price.setter
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
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity_in_stock})'


    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        name = product_data["name"]
        description = product_data["descriptoin"]
        price = product_data["price"]
        quantity_in_stock = product_data["quantity_in_stock"]
        if list_of_products:
            for product in list_of_products:
                if product_data == name:
                    product.quantity_in_stock += quantity_in_stock
                    if product.price < price:
                        product.price = price
                    return product
        new_product = cls(name, description, price, quantity_in_stock)
        return new_product