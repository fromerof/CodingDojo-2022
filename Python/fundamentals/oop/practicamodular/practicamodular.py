class Padre:
    def method_a(self):
        print("invocando método_a PADRE")
class Hijo(Padre):
    def method_a(self):
        print("invocando método_a HIJO")
papá = Padre()
hijo = Hijo()
papá.method_a()
hijo.method_a() # Nota que esto anula el método Padre

