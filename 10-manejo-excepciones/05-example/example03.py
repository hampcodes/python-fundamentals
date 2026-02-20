class EdadInvalidaError(Exception):
    def __init__(self, edad):
        super().__init__(f'Edad {edad} no valida')

def ingresar_edad(edad):
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(edad)

try:
    ingresar_edad(-5)
except EdadInvalidaError as e:
    print(f'Error: {e}')  # Error: Edad no valida