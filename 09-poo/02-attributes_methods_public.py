# Atributos: son las variables que pertenecen al objeto.
#            Almacenan los datos de cada cuenta (holder, balance).
#
# Metodos publicos: son funciones dentro de la clase que definen
#                   el comportamiento del objeto. Cualquiera puede
#                   usarlos desde fuera de la clase.

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder      # Atributo
        self.balance = balance    # Atributo

    # Metodo publico
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    # Metodo publico
    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
            return
        self.balance -= amount
        print(f"Retiro de S/{amount:.2f} realizado")

    def __str__(self):
        return f"{self.holder} | S/{self.balance:.2f}"


# Creando objetos
account1 = BankAccount("Ana Lopez", 1000)
account2 = BankAccount("Carlos Ruiz", 2500)

# Mostrando estado inicial
print("--- Estado inicial ---")
print(account1)
print(account2)

# Usando metodos publicos
print("\n--- Operaciones ---")
account1.deposit(300)
account2.withdraw(500)
account2.withdraw(5000)

# Mostrando estado final
print("\n--- Estado final ---")
print(account1)
print(account2)
