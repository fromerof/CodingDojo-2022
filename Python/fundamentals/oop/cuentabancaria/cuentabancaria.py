class CuentaBancaria:
    listaInstancias = []

    def __init__(self,cuenta):
        self.cuenta = cuenta
        self.balance = 0
        self.tasa_interes = 0
        CuentaBancaria.listaInstancias.append(self)

    def deposito(self,amount):
        self.balance += amount
        CuentaBancaria.listaInstancias.append(self)
        return self
        
    
    def retiro(self,amount):
        if self.balance > 0:
            self.balance -= amount 
            return self
        elif self.balance < 0:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self
        CuentaBancaria.listaInstancias.append(self)
    def generar_interes(self,tasa_interes):
        if self.balance > 0:
            self.balance = self.balance*(1+tasa_interes)
            return self
        CuentaBancaria.listaInstancias.append(self)
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        CuentaBancaria.listaInstancias.append(self)
    #@classmethod #ni idea
    #def totalInstances(cls):
        #for i in CuentaBancaria.listaInstancias:
            #print(CuentaBancaria.listaInstancias[i])


cuenta1 = CuentaBancaria("Cuenta1")
cuenta2 = CuentaBancaria("Cuenta2")
cuenta1.deposito(500).deposito(500).deposito(500).retiro(300).generar_interes(0.5).mostrar_info_cuenta()
cuenta2.deposito(2500).deposito(2500).retiro(500).retiro(500).retiro(500).retiro(500).generar_interes(0.3).mostrar_info_cuenta()

print(CuentaBancaria.listaInstancias.__dir__)
#print(CuentaBancaria.listaInstancias[0].)
