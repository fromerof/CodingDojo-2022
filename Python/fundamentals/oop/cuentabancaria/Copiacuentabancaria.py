class CuentaBancaria:
    def __init__(self,tasa_interes,balance):
        self.cuenta = ""
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

nombreCuenta = CuentaBancaria.cuenta = "Felipe"
cuenta1 = CuentaBancaria(0,0)
cuenta1.deposito(500).deposito(500).deposito(500).retiro(300).generar_interes(0.5).mostrar_info_cuenta()
print(nombreCuenta)


