from custom_exceptions import InvalidValueError

#Aquí sí necesitamos el setter de stock porque product_service.py necesita modificarlo desde afuera.
class Product:
    def __init__(self, name, price, stock):
        if price <= 0:
            raise InvalidValueError("precio", price)
        if stock < 0:
            raise InvalidValueError("stock", stock)
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise InvalidValueError("precio", new_price)
        self.__price = new_price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise InvalidValueError("stock", new_stock)
        self.__stock = new_stock

    def __str__(self):
        return f"{self.__name} | Precio: ${self.__price:.2f} | Stock: {self.__stock}"