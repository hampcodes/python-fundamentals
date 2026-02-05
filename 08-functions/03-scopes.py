print("=== Scope de Variables ===")

global_var = "Soy una variable global"  # Variable global

def my_function():
    local_var = "Soy una variable local"  # Variable local (solo existe dentro de la funcion)
    print("Dentro de la funcion:")
    print(global_var)  # Se puede usar porque es global
    print(local_var)   # Se puede usar porque es local

my_function()

print("\nFuera de la funcion:")
print(global_var)  # Funciona fuera porque es global
# print(local_var)  # ERROR: local_var no existe fuera de la funcion
