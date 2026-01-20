# 4. Índices de cadenas (string indexes)
# Las cadenas son secuencias de caracteres, y cada carácter tiene un índice asociado.

name = "Henry"

# Índices del string:
# H   e   n   r   y
# 0   1   2   3   4

# print(name)  # Henry

# print(name[0])  # H
# print(name[1])  # e
# ...
# print(name[4])  # y

# ¿Cómo obtener la última letra?
# print(name[-1])

# ¿Cómo obtener la penúltima letra? 
# print(name[-2])
# Slicing: obtener subcadenas usando índices [Start:Stop(:Step)]
# Henry
# Hen
# [Start:Stop]
# Empieza en el índice 0 (H) y se detiene antes del índice 3 (r):
# print(name[0:3])

# [Start:Stop:Step]
# Empieza en el índice 0 (H) y avanza de 2 en 2:
# 0 → H
# 0 + 2 = 2 → n
# Se detiene antes del índice 3
print(name[0:3:2])  # Hn

# ¿Cómo puedo poner mi nombre al revés?

# [Start:Stop:Step]
# Usar :: indica que no hay inicio ni fin y que se recorre toda la cadena
# con un paso de -1, lo que invierte el texto
#name_reverse = f"{name[4]}{name[3]}{name[2]}{name[1]}{name[0]}"
# Alternativamente, se puede usar slicing con paso negativo:
# slicing es una técnica para obtener subcadenas
name_reverse = name[::-1]

print(name_reverse)  # yrenH