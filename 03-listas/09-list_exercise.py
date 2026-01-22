# Gestor de películas favoritas

print("Gestor de películas favoritas")
print("Opciones: ")
print("1. Agregar película")
print("2. Eliminar película")
print("3. Mostrar la lista ordenada")
print("4. Buscar película")
print("5. Contar películas")
print("6. Vaciar la lista")

movies = ["Inception", "Titanic", "Matrix", "Avatar"]
option = input("Elige una opción (1-6): ")

if option == "1":
    movie = input("Ingresa el nombre de la película: ")
    if movie not in movies:
        movies.append(movie)
        print("Película agregada")
    else:
        print("La película ya está en la lista")

elif option == "2":
    movie = input("Ingresa el nombre de la película a eliminar: ")
    if movie in movies:
        movies.remove(movie)
        print("Película eliminada")
    else:
        print("La película no está en la lista")

elif option == "3":
    if len(movies) > 0:
        print("Lista de películas ordenada:")
        movies.sort()
        print(movies)
    else:
        print("La lista está vacía")

elif option == "4":
    movie = input("Ingresa el nombre de la película a buscar: ")
    if movie in movies:
        print(f"'{movie}' está en la lista de películas")
    else:
        print("Película no encontrada")

elif option == "5":
    print("Total de películas:", len(movies))

elif option == "6":
    movies.clear()
    print("Lista de películas vaciada")

else:
    print("Opción no válida.")

print("Estado final de la lista de películas:")
print(movies)
