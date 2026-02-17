from custom_exceptions import InvalidValueError, InsufficientStockError


class ProductService:

    @staticmethod
    def add_stock(product, quantity):
        if quantity <= 0:
            raise InvalidValueError("cantidad", quantity)
        product.stock += quantity
        print(f"  + {quantity} unidades agregadas a '{product.name}'. Stock: {product.stock}")

    @staticmethod
    def withdraw_stock(product, quantity):
        if quantity <= 0:
            raise InvalidValueError("cantidad", quantity)
        if quantity > product.stock:
            raise InsufficientStockError(product.name, product.stock, quantity)
        product.stock -= quantity
        total = quantity * product.price
        print(f"  - {quantity} unidades retiradas de '{product.name}'. Total: ${total:.2f}. Stock: {product.stock}")