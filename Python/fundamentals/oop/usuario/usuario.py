class Usuario:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.amount = 0
    def hacer_deposito(self,amount):
        self.balance += amount
        return self
        
    def hacer_retiro(self,amount):
        self.balance -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, balance {self.balance}")
    
    def transferir_dinero(self,amount,usuario): #visto en la solucion
        self.balance -= amount
        usuario.balance += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()


felipe = Usuario("Felipe")
zeus = Usuario("Zeus")
jack = Usuario("Jack")

felipe.hacer_deposito(1000).hacer_deposito(400).hacer_deposito(300).hacer_retiro(700).mostrar_balance_usuario()

zeus.hacer_deposito(1000).hacer_deposito(11000).hacer_retiro(5000).hacer_retiro(3000).mostrar_balance_usuario()

jack.hacer_deposito(50000).hacer_retiro(10000).hacer_retiro(10000).hacer_retiro(10000).mostrar_balance_usuario()

felipe.transferir_dinero(300,jack)


