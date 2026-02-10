class BankAccount:
    bank_name = "CEIPRO Bank"  # atributo de clase

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        # classmethod: cambia un dato de la clase (afecta a todas las cuentas)
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        # staticmethod: valida un dato (no usa self ni cls)
        return amount > 0

    def deposit(self, amount):
        # método normal: usa self porque modifica el balance del objeto
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print("Depósito exitoso")
        else:
            print("Monto inválido")


account1 = BankAccount("Henry", 1000)
account2 = BankAccount("Patricia", 500)

print(BankAccount.bank_name)

BankAccount.change_bank_name("CEIPRO Banco Oficial")
print(BankAccount.bank_name)

account1.deposit(200)
account2.deposit(-50)

print(account1.balance)
print(account2.balance)
