try:
    edad = int(input('Ingresa tu edad: '))
    if edad < 0 or edad > 150:
        print('Edad no valida')
    resultado = 10 / 2
    print(f'Tu edad es: {edad}')
    print(f'Resultado: {resultado}')
except ValueError:
    print('Eso no es un numero')
except ZeroDivisionError:
    print('No se puede dividir por cero')
finally:
    print('Fin')

