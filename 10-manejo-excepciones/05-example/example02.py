def ingresar_edad(edad):
    if edad < 0 or edad > 150:
        print('Edad no valida')  # solo imprime, no avisa
        #raise ValueError('Edad no valida')
    print(f'Edad {edad} guardada')


try:
    ingresar_edad(-5)
except ValueError as e:
    print(f'Error: {e}')  # Error: Edad no valida
