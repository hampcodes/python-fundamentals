with open('datos.txt', 'w') as f:
    f.write('Laptop|2500\n')
    f.write('Mouse|35\n')

with open('datos.txt', 'r') as f:
    for linea in f:
        print(linea.strip())

try:
    with open('datos.txt', 'r') as f:
        for linea in f:
            partes = linea.strip().split('|')
            print(f'{partes[0]} - ${partes[1]}')
except FileNotFoundError:
    print('El archivo no existe')
