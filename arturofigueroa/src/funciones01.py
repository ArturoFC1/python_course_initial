#Funcion
def saludar(nombre: str) -> str:  #sirve para dar a conocer que va a retornar una pista documentar
    '''Funcion que devuelve un saludo'''
    return f"Hola {nombre}"

print(saludar("Arturo"))
    
#Guncion con argumento default    
def saludo_generico(nombre = "Usuario"):
    return f"Hola {nombre}"

print(saludo_generico("Jonh"))

#Funcion con argumento kwargs


#lambda

def suma(n1: int, n2: int) -> int:
    return n1+n2

suma_lambda = lambda n1,n2 : n1+n2

print(suma(2,3))
print(suma_lambda(3,2))

#MAP Y FILTER


#Map 
lista_numeros = [1,2,3,4,5]

tipo_dato = type((map(lambda x: x**2,lista_numeros)))
print(f"Tipo de dato: {tipo_dato}")

cuadrados = list(map(lambda x: x**2,lista_numeros))
print(cuadrados)

#Filter

pares = list(filter(lambda x: x%2 == 0), lista_numeros)
print(pares)

