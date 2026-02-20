class ArchivoError(Exception):
    def __init__(self,nombre_archivo, mensaje):
        super().__init__(f"Error en el archivo {nombre_archivo} {mensaje}")


# Escribir
def escribir_datos(nombre_archivo:str, productos: list):
    with open(nombre_archivo,'w') as f:
        #f.write('Laptop|2500\n')
        #f.write('Laptop|2500\n')
        #f.write('Teclado|35\n')
        for p in productos:
            f.write(f"{p['nombre']}| {p['precio']}\n")
    print(f"Archivo {nombre_archivo} guardado con {len(productos)} productos")

# Agregar
def agregar_datos(nombre_archivo:str, productos: list):
    with open(nombre_archivo,'a') as f:
        for p in productos:
            f.write(f"{p['nombre']}| {p['precio']}\n")
    print(f"{len(productos)} productos agregados al archivo {nombre_archivo}")
    
# Leer
def leer_archivo(nombre_archivo:str):
    if not nombre_archivo.endswith(".txt"):
        #raise FileNotFoundError(nombre_archivo, "Debe ser un archivo .txt")
        raise ArchivoError(nombre_archivo, "Debe ser un archivo .txt")
    
    with open(nombre_archivo,'r') as f:
        for linea in f:
            #print(linea.strip())
            partes = linea.strip().split('|')
            #print(len(partes))
            if (len(partes) < 2):
                raise ArchivoError(nombre_archivo, f"Linea mal formateada: {linea.strip()}")
            print(f"{partes[0]} - S/.{partes[1]}")

def mostrar_menu():
    print('\n=== GESTOR DE PRODUCTOS ===')
    print('1. Escribir productos (sobreescribe)')
    print('2. Agregar productos')
    print('3. Leer archivo')
    print('4. Salir')
    return input('Opcion: ').strip()

productos = [
    {"nombre":"Laptop", "precio": 2500},
    {"nombre":"Mouse", "precio": 35},
    {"nombre":"Teclado", "precio": 35}
]

nuevos_productos = [
    {"nombre":"Monitor", "precio": 800},
    {"nombre":"Audifonos", "precio": 120}
]


ARCHIVO = 'datos.txt'

while True:
    opcion = mostrar_menu()

    try:
        if opcion == '1':
            escribir_datos(ARCHIVO, productos)
        elif opcion == '2':
            agregar_datos(ARCHIVO, nuevos_productos)
        elif opcion == '3':
            leer_archivo(ARCHIVO)
        elif opcion == '4':
            print('Hasta luego!')
            break
        else:
            print('Opcion no valida')
    except ArchivoError as e:
        print(e)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")