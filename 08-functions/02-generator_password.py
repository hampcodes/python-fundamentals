
#  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  numeros = "0123456789"
#  simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres = letras + numeros + simbolos
# Formula simple: (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida : &D^#23SN

import string
import random


# Funcion que RETORNA la contrasena generada
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
    #for _ in range(length):
        password += random.choice(chars)

    return password


# Funcion que NO retorna nada (solo imprime en pantalla)
def show_result(password):
    print("Tu contrasena segura es:", password)


length = int(input("Cuantos caracteres quieres en tu contrasena? "))

password = generate_password(length)
show_result(password)
