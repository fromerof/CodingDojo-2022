
#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 

a = x[0]
b = x[1]
b[0] = 15
print(x)

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name'] = "Bryant"
print(estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = "Andrés"
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30
print(z)


#2 Iterar a través de una lista de diccionarios
def iterateDictionary(estudiantes):
    for i in estudiantes:
        print('first_name -', i['first_name'] + ', ' + 'last_name -',i['last_name']) 
        


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary(estudiantes)


#3 Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for i in estudiantes:
        print(i[key_name])



estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2("first_name",estudiantes)
iterateDictionary2("last_name",estudiantes)

#4 Iterar a través de un diccionarios con valores de lista

def locations(some_dict):
    for keys in dojo:
        print(len(dojo[keys]),keys.upper())
        for i in dojo[keys]:
            print(i[:])



dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
locations(dojo)

