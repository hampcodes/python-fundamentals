class InvalidValueError(Exception):
    def __init__(self, field, value):
        super().__init__(f"Valor inválido en {field}: {value}. Debe ser mayor a cero.")


class InsufficientStockError(Exception):
    def __init__(self, product_name, stock, requested):
        super().__init__(
            f"Stock insuficiente para '{product_name}'. "
            f"Disponible: {stock}, Solicitado: {requested}."
        )