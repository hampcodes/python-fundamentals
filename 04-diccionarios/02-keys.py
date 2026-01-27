# Diccionario que representa a un usuario
user = {
    "name": "Henry",
    "age": 45,
    "email": "hmendo81@email.com",
    "active": True,
    (19.12, -89.33): "Lima"  # Clave tipo tupla (inmutable)
}

print(user)  # Muestra todo el diccionario

# Modificar valores usando claves existentes
user["name"] = "Hamp"   
user["age"] = 44       

# Agregar una nueva clave con su valor.
# Crea la clave si no existe; si existe, actualiza su valor.
user["country"] = "Perú"

# Acceder a un valor usando una clave tipo tupla
print(user[(19.12, -89.33)])  # Lima
