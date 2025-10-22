import time

#Decaoradores funcion que proporciona otra funcion

"""""
print("Time", time.time())
sum([i**2 for i in range(100000)])
print("Time", time.time)

"""""
def saludo():
    print("Hola mundo")


def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("Final")
    return envoltura

@decorador
def saludo():
    print("Hola mundo")

saludo()
