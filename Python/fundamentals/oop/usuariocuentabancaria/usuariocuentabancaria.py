class CuentaBancaria:
    def __init__(self,tasa_interes,balance):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self,amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if self.balance > 0:
            self.balance -= amount 
            return self
        elif self.balance < 0:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self
    def generar_interes(self,tasa_interes):
        if self.balance > 0:
            self.balance = self.balance*(1+tasa_interes)
            return self
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
    
    @classmethod #ni idea
    def totalInstances(cls):
        for i in cls.CuentaBancaria:
            print(i)
        return i

class Usuario:
    def __init__(self,name):
        self.name = name
        self.amount = 0
        self.cuenta = CuentaBancaria(0,0)

    def hacer_deposito(self,amount):
        self.cuenta.balance += amount
        return self
        
    def hacer_retiro(self,amount):
        self.cuenta.balance -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, balance {self.cuenta.balance}")

cuenta1 = Usuario("Cuenta Corriente")
cuenta2 = Usuario("Savings")
cuenta1.cuenta.deposito(1000).retiro(100).generar_interes(0.3)
cuenta1.hacer_deposito(1000).hacer_retiro(800)
cuenta1.mostrar_balance_usuario()
cuenta2.cuenta.deposito(10000).retiro(800).generar_interes(0.5)
cuenta2.mostrar_balance_usuario()










