import openpyxl
 
class GastoError(Exception):
    def __init__(self, campo, mensaje):
        self.campo = campo
        self.mensaje = mensaje
        super().__init__(f'Error en {campo}: {mensaje}')

class Gasto:
    CATEGORIAS = ['comida', 'transporte', 'salud', 'educacion', 'otro']
 
    def __init__(self, descripcion, monto, categoria):
        if not descripcion:
            raise GastoError('descripcion', 'no puede estar vacia')
        if monto <= 0:
            raise GastoError('monto', 'debe ser mayor a 0')
        if categoria not in Gasto.CATEGORIAS:
            raise GastoError('categoria', f'debe ser una de {Gasto.CATEGORIAS}')
 
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
 
    def __str__(self):
        return f'{self.descripcion} - S/{self.monto:.2f} ({self.categoria})'

# --- Crear gastos validos ---
gastos = []
 
gastos.append(Gasto('Almuerzo', 15.50, 'comida'))
gastos.append(Gasto('Taxi', 8.00, 'transporte'))
gastos.append(Gasto('Cafe', 5.00, 'comida'))
 
print('Gastos registrados:')
for g in gastos:
    print(f'  {g}')


# --- Intentar crear gastos invalidos ---
print('\nProbando validaciones:')
 
try:
    gasto_malo = Gasto('', 10, 'otro')
except GastoError as e:
    print(f'  {e}')
 
try:
    gasto_malo = Gasto('Cena', -20, 'comida')
except GastoError as e:
    print(f'  {e}')
 
try:
    gasto_malo = Gasto('Regalo', 50, 'lujo')
except GastoError as e:
    print(f'  {e}')


# --- Guardar en Excel ---
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Gastos'
 
ws.append(['Descripcion', 'Monto', 'Categoria'])
 
for g in gastos:
    ws.append([g.descripcion, g.monto, g.categoria])
 
total = sum(g.monto for g in gastos)
ws.append([])
ws.append(['TOTAL', total, ''])
 
wb.save('gastos.xlsx')
print(f'\nArchivo gastos.xlsx guardado con {len(gastos)} gastos')


# --- Guardar en TXT ---
with open('gastos.txt', 'w') as f:
    f.write('REGISTRO DE GASTOS\n')
    f.write('-' * 40 + '\n')
    for g in gastos:
        f.write(f'{g.descripcion}|{g.monto}|{g.categoria}\n')
    f.write(f'\nTOTAL: S/{total:.2f}\n')
 
print('Archivo gastos.txt guardado')
