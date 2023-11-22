
class Producto:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def actualizar_precio(self,cambio_porcentaje,esta_elevado):
        self.cambio_porcentaje = cambio_porcentaje
        self.esta_elevado = esta_elevado
        if esta_elevado == True:
            self.price = self.price*(1+cambio_porcentaje)
        if esta_elevado == False:
            self.price = self.price*(1-cambio_porcentaje)
        return self
    def print_info(self):
        print(f"Nombre Producto: {self.name}\nCategory: {self.category}\nPrice: {self.price}")
        return self


class Tienda:
    def __init__(self,nombreTienda,producto):
        self.nombreTienda = nombreTienda
        self.producto = producto
        self.listaProductos = []
    def agregar_producto(self,nuevo_producto):
        tienda.listaProductos.append(nuevo_producto)
        return self
    def vender_producto(self,id):
        pass

producto = Producto("Portal gun",1000,"Travel")
tienda = Tienda("Intergalatic Shop",producto)
producto.actualizar_precio(0.03,False).print_info()
tienda.agregar_producto(producto)
print(tienda.listaProductos.__str__)


