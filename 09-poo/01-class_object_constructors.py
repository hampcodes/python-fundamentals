# self: referencia al objeto actual, permite que cada objeto
#       acceda a sus propios datos (holder, balance)
#
# __init__: constructor, se ejecuta automaticamente al crear
#           un objeto. Inicializa los atributos con self
#
# __str__: define como se muestra el objeto al usar print().
#          Sin este metodo se mostraria algo como:
#          <__main__.BankAccount object at 0x7f...>

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"{self.holder} | S/{self.balance:.2f}"


# Creando objetos
account1 = BankAccount("Ana Lopez", 1000)
account2 = BankAccount("Carlos Ruiz", 2500)
account3 = BankAccount("Maria Torres", 800)

# Mostrando los objetos
print(account1)
print(account2)
print(account3)

# Accediendo a atributos
print(f"\nTitular: {account1.holder}")
print(f"Saldo: S/{account1.balance:.2f}")