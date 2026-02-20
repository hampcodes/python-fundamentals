class EdadInvalidaError(Exception):
    def __init__(self,edad):
        super().__init__(f"Edad {edad} no valida")


def ingresar_edad(edad:int):
    if edad < 0 or edad > 100:
        #raise ValueError("Edad no valida")
        raise EdadInvalidaError(edad)
    print(f"Tu edad es: {edad}")
    
try:
    ingresar_edad(-5)
#except ValueError as e:
except EdadInvalidaError as e:
     print(f"Error: {e}")
     

try:
    edad = int(input("Ingresa tu edad:"))
    numero_1 = int(input("Ingresa numero uno:"))
    numero_2 = int(input("Ingresa numero dos:"))
    resultado = numero_1 / numero_2
    print(f"Tu edad es: {edad}")
except ValueError:
    print("Eso no es un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Este bloque se ejecuta exista o no exception")
        
print("fin")
