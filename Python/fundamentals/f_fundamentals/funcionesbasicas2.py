#1 Cuenta Regresiva
lista = []
def regresiva(num):
    for i in range(num,0,-1):
        lista.append(i)
    return lista

cuentaRegresiva = regresiva(10)
print(cuentaRegresiva)

# 2 Imprimir y devolver
def devolver(lista):
    print(lista[0])
    return lista[1]

lista = [3,9]
unoDos = devolver(lista)
print(unoDos)

#3 Primero mas longitud
def suma(lista):
    return lista[0] + len(lista)

lista = [3,6,9]
imprimir = suma(lista)
print(imprimir)

#4 Valores mayores que el segundo
def valores(lista):
    newList = []
    for i in lista:
        if len(lista) < 2:
            return False
        elif i > lista[1]:
            newList.append(i)
    print(len(newList)) 
    return newList

print(valores([3,2,7,20,1,9]))
print(valores([3]))

# 5 Esta longtiud, ese valor

def cinco(size,value):
    lista = []
    for i in range(0,size):
        lista.append(value)
    return lista


print(cinco(4,7))
print(cinco(6,2))



