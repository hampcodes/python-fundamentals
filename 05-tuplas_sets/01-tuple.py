# Tupla con datos de una película
movie = ("Inception", 2010, "Christopher Nolan", 8.8, "Science Fiction")
print(movie)

# Acceder a elementos por índice
title = movie[0]
year = movie[1]
director = movie[2]
rating = movie[3]
genre = movie[4]

# Mostrar datos
print(f"Title: {title}")
print(f"Year: {year}")
print(f"Director: {director}")
print(f"Rating: {rating}")
print(f"Genre: {genre}")

# Métodos de tuplas:

# .count() - Cuenta cuántas veces aparece un elemento
print(movie.count(2010))  # Resultado: 1

# .index() - Devuelve el índice de la primera aparición de un elemento
print(movie.index("Christopher Nolan"))  # Resultado: 2

# movie[0] = "Avatar"  # ESTO NO SE PUEDE - Las tuplas son inmutables

# Las tuplas no pueden cambiar
# movie[0] = "Interstellar"  # Error

# Por eso SÍ se pueden agregar a un set
movies_set = {("Inception", 2010), ("Avatar", 2009), ("Titanic", 1997)}
print(movies_set)

# Las listas SÍ pueden cambiar
# mi_lista = ["Inception", 2010]
# mi_lista[0] = "Avatar"  # Se puede modificar

# Por eso NO se pueden agregar a un set
# movies_set = {["Inception", 2010], ["Avatar", 2009]}  # ESTO NO SE PUEDE - Error