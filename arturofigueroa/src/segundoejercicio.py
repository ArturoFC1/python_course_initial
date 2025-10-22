#Serie de fibonacci

def fibonacci_funcion(limite: int):
    print("Inicio de funcion tradicional")
    a, b = 0, 1
    for i in range(limite):
        print("Posicion", i, "->", a)
        a, b = b, a + b
    print("Fin de funcion tradicional")

fibonacci_funcion(10)
