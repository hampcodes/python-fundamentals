print("=== Sistema de Contactos ===")


# Funcion que NO retorna nada (solo imprime el menu)
def show_menu():
    print("\n--- MENU ---")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")


# Funcion que RETORNA un valor (True/False)
def contact_exists(contacts, name):
    return name in contacts


# Funcion que NO retorna nada (agrega contacto)
def add_contact(contacts, name, phone):
    if contact_exists(contacts, name):
        print("Error: el contacto ya existe.")
    else:
        contacts[name] = phone
        print("Contacto agregado correctamente!")


# Funcion que NO retorna nada (elimina contacto)
def delete_contact(contacts, name):
    if contact_exists(contacts, name):
        contacts.pop(name)
        print("Contacto eliminado correctamente!")
    else:
        print("Error: contacto no encontrado.")


# Funcion que NO retorna nada (busca contacto)
def search_contact(contacts, name):
    if contact_exists(contacts, name):
        print(f"Contacto encontrado: {name} -> {contacts[name]}")
    else:
        print("Contacto no encontrado.")


# Funcion que NO retorna nada (muestra contactos)
def show_contacts(contacts):
    print("\n=== Lista de Contactos ===")

    if len(contacts) == 0:
        print("No hay contactos registrados.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


contacts = {}  # Diccionario: nombre -> telefono
option = ""

while option != "5":

    show_menu()
    option = input("Elige una opcion: ")

    if option == "1":
        name = input("Ingrese nombre del contacto: ")
        phone = input("Ingrese telefono: ")
        add_contact(contacts, name, phone)

    elif option == "2":
        name = input("Ingrese nombre del contacto a eliminar: ")
        delete_contact(contacts, name)

    elif option == "3":
        name = input("Ingrese nombre a buscar: ")
        search_contact(contacts, name)

    elif option == "4":
        show_contacts(contacts)

    elif option == "5":
        print("Adios!")

    else:
        print("Opcion invalida. Intente nuevamente.")
