# HERENCIA + CLASE ABSTRACTA + POLIMORFISMO con Menu
#
# CLASE ABSTRACTA: es una clase que NO se puede instanciar directamente.
#   Su proposito es servir como plantilla para las clases hijas.
#   Define metodos abstractos que las hijas ESTAN OBLIGADAS a implementar.
#   Si una hija no implementa el metodo abstracto, Python lanza error.
#
# HERENCIA: las clases hijas (SavingsAccount, CheckingAccount, BusinessAccount)
#   heredan todos los atributos y metodos de la clase padre (BankAccount).
#   Esto evita repetir codigo comun como deposit(), withdraw() y __str__().
#   Se usa super().__init__() para reutilizar el constructor del padre.
#
# POLIMORFISMO: significa "muchas formas". El metodo calculate_fee() existe
#   en todas las cuentas, pero cada una lo implementa con logica diferente.
#   Cuando llamamos withdraw(), Python ejecuta automaticamente la version
#   correcta de calculate_fee() segun el tipo de cuenta, sin necesidad
#   de usar if/elif para preguntar que tipo de cuenta es.
#
# from abc import ABC, abstractmethod:
#   abc = modulo de Python para trabajar con clases abstractas
#   ABC = clase base que convierte nuestra clase en abstracta
#   abstractmethod = decorador (@abstractmethod) que marca un metodo
#                    como obligatorio para las clases hijas
#
# Enunciado:
# Un banco tiene 3 tipos de cuenta con diferente comision al retirar:
# - Ahorro: 3 retiros gratis, luego S/5
# - Corriente: 1.5% fijo
# - Empresarial: tramos (2%, 1%, 0.5%)
#
# NIVELES DE ACCESO en Python (convencion):
#   public    = sin guion bajo (ej: deposit, withdraw)
#              -> accesible desde cualquier parte
#   protected = un guion bajo _  (ej: _holder, _balance)
#              -> accesible por la clase y sus hijas (herencia)
#   private   = doble guion bajo __ (ej: __withdrawal_count)
#              -> solo accesible dentro de su propia clase

from abc import ABC, abstractmethod


# --- CLASE ABSTRACTA (PADRE) ---
# BankAccount: clase base abstracta que define la estructura comun
# de todas las cuentas bancarias. No se puede crear objetos de esta clase.
class BankAccount(ABC):

    # Constructor: inicializa el titular y saldo de la cuenta
    # _holder y _balance son PROTECTED (un _) porque las hijas
    # necesitan acceder a ellos (ej: en __str__ de cada hija)
    def __init__(self, holder, balance):
        self._holder = holder       # protected: accesible por hijas
        self._balance = balance     # protected: accesible por hijas

    # deposit: agrega dinero a la cuenta
    def deposit(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return
        self._balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    # withdraw: retira dinero descontando la comision segun el tipo de cuenta
    def withdraw(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return
        fee = self.calculate_fee(amount)  # POLIMORFISMO: cada hijo calcula distinto
        total = amount + fee
        if total > self._balance:
            print("Fondos insuficientes")
            return
        self._balance -= total
        print(f"Retiro de S/{amount:.2f} + Comision S/{fee:.2f}")

    # calculate_fee (fee = comision): metodo abstracto que cada hija
    # debe implementar con su propia logica para calcular la comision
    @abstractmethod
    def calculate_fee(self, amount):
        pass

    # __str__: representacion en texto de la cuenta (se ejecuta con print)
    def __str__(self):
        return f"{self._holder} | Saldo: S/{self._balance:.2f}"


# --- CLASES HIJAS (HERENCIA) ---

# SavingsAccount (Cuenta de Ahorro): hereda de BankAccount
# Regla: 3 retiros gratis al mes, luego cobra S/5 por cada retiro adicional
class SavingsAccount(BankAccount):
    FREE_WITHDRAWALS = 3

    # Constructor: llama al padre con super() y agrega contador de retiros
    def __init__(self, holder, balance):
        super().__init__(holder, balance)
        self.__withdrawal_count = 0  # private: solo lo usa esta clase

    # calculate_fee: si supera los 3 retiros gratis, cobra S/5
    #def calculate_fee(self, amount):
    #    self.__withdrawal_count += 1
    #    fee = 5.00 if self.__withdrawal_count > self.FREE_WITHDRAWALS else 0
    #    return fee

    # calculate_fee: si supera los 3 retiros gratis, cobra S/5
    def calculate_fee(self, amount):
        self.__withdrawal_count += 1
        if self.__withdrawal_count > self.FREE_WITHDRAWALS:
            return 5.00
        return 0

    # __str__: muestra datos de la cuenta + cantidad de retiros realizados
    def __str__(self):
        return f"[Ahorro] {super().__str__()} | Retiros: {self.__withdrawal_count}"


# CheckingAccount (Cuenta Corriente): hereda de BankAccount
# Regla: cobra comision fija de 1.5% sobre el monto retirado
class CheckingAccount(BankAccount):
    COMMISSION = 0.015

    # calculate_fee: retorna el 1.5% del monto como comision
    def calculate_fee(self, amount):
        return amount * self.COMMISSION

    # __str__: muestra datos de la cuenta corriente
    def __str__(self):
        return f"[Corriente] {super().__str__()}"


# BusinessAccount (Cuenta Empresarial): hereda de BankAccount
# Regla: comision por tramos segun el monto retirado
class BusinessAccount(BankAccount):

    # calculate_fee: hasta S/1000 cobra 2%, hasta S/5000 cobra 1%, mas cobra 0.5%
    def calculate_fee(self, amount):
        if amount <= 1000:
            return amount * 0.02
        elif amount <= 5000:
            return amount * 0.01
        else:
            return amount * 0.005

    # __str__: muestra datos de la cuenta empresarial
    def __str__(self):
        return f"[Empresarial] {super().__str__()}"


# --- FUNCIONES DEL MENU ---

# create_account: pide al usuario el tipo de cuenta, titular y saldo
# inicial, y retorna el objeto de cuenta creado
def create_account():
    print("\nTipo de cuenta:")
    print("1. Ahorro")
    print("2. Corriente")
    print("3. Empresarial")
    tipo = input("Seleccione: ")
    nombre = input("Titular: ")
    saldo = float(input("Saldo inicial: S/"))

    if tipo == "1":
        return SavingsAccount(nombre, saldo)
    elif tipo == "2":
        return CheckingAccount(nombre, saldo)
    elif tipo == "3":
        return BusinessAccount(nombre, saldo)
    else:
        print("Opcion invalida")
        return None


# list_accounts: muestra la lista numerada de cuentas registradas
def list_accounts(accounts):
    print("\n--- Cuentas registradas ---")
    for i, acc in enumerate(accounts):
        print(f"{i + 1}. {acc}")



# menu: funcion principal que muestra las opciones del sistema bancario
# y ejecuta la accion que el usuario elija en un bucle infinito
def menu():
    accounts = []

    while True:
        print("\n===== BANCO - MENU =====")
        print("1. Crear cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver todas las cuentas")
        print("5. Salir")
        option = input("Seleccione: ")

        if option == "1":
            account = create_account()
            if account:
                accounts.append(account)
                print("Cuenta creada exitosamente")

        elif option == "2":
            if not accounts:
                print("No hay cuentas registradas")
                continue
            # TODO: este bloque se puede migrar a una funcion choose_account()
            list_accounts(accounts)
            index = int(input("Seleccione cuenta: ")) - 1
            if 0 <= index < len(accounts):
                amount = float(input("Monto a depositar: S/"))
                accounts[index].deposit(amount)

        elif option == "3":
            if not accounts:
                print("No hay cuentas registradas")
                continue
            # TODO: este bloque se puede migrar a una funcion choose_account()
            list_accounts(accounts)
            index = int(input("Seleccione cuenta: ")) - 1
            if 0 <= index < len(accounts):
                amount = float(input("Monto a retirar: S/"))
                accounts[index].withdraw(amount)  # POLIMORFISMO en accion

        elif option == "4":
            if not accounts:
                print("No hay cuentas registradas")
                continue
            list_accounts(accounts)

        elif option == "5":
            print("Gracias por usar el banco")
            break

        else:
            print("Opcion invalida")


menu()



# --- EJEMPLO DE PRUEBA (comentado) ---
# Para probar sin menu, descomentar las siguientes lineas y comentar menu()
#
# # Crear cuentas
# ahorro = SavingsAccount("Ana Lopez", 2000)
# corriente = CheckingAccount("Carlos Ruiz", 5000)
# empresarial = BusinessAccount("Empresa SAC", 10000)
#
# # Estado inicial
# print("--- Estado inicial ---")
# print(ahorro)       # [Ahorro] Ana Lopez | Saldo: S/2000.00 | Retiros: 0
# print(corriente)    # [Corriente] Carlos Ruiz | Saldo: S/5000.00
# print(empresarial)  # [Empresarial] Empresa SAC | Saldo: S/10000.00
#
# # Cuenta de Ahorro: 3 retiros gratis, el 4to cobra S/5
# print("\n--- Retiros en cuenta de ahorro ---")
# ahorro.withdraw(100)  # Retiro 1: gratis      -> comision S/0.00
# ahorro.withdraw(100)  # Retiro 2: gratis      -> comision S/0.00
# ahorro.withdraw(100)  # Retiro 3: gratis      -> comision S/0.00
# ahorro.withdraw(100)  # Retiro 4: cobra S/5   -> comision S/5.00
#
# # Cuenta Corriente: siempre cobra 1.5%
# print("\n--- Retiro en cuenta corriente ---")
# corriente.withdraw(1000)  # 1.5% de 1000 = S/15.00
#
# # Cuenta Empresarial: comision por tramos
# print("\n--- Retiros en cuenta empresarial ---")
# empresarial.withdraw(500)   # 2% de 500   = S/10.00
# empresarial.withdraw(3000)  # 1% de 3000  = S/30.00
# empresarial.withdraw(6000)  # 0.5% de 6000 = S/30.00
#
# # Depositar
# print("\n--- Depositos ---")
# ahorro.deposit(500)  # Deposito de S/500.00 realizado
#
# # Estado final
# print("\n--- Estado final ---")
# print(ahorro)
# print(corriente)
# print(empresarial)
