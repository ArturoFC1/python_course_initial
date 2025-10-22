# yield

def conteo_to_limit(limit: int):
    'Cuenta desde cero hasta el límite (versión tradicional)'
    print("Inicio de función tradicional")
    numeros = []  # lista donde guardaremos los valores
    for i in range(limit):
        print("En la posición", i)
        numeros.append(i)
    print("Finaliza la función tradicional")
    return numeros


def conteo_gen(limit: int):
    'Cuenta desde cero hasta el límite (versión generador)'
    print("Inicio del generador")
    for i in range(limit):
        print("En la posición", i)
        yield i  # 'yield' devuelve un valor sin cerrar la función
    print("Fin del generador")


# Llamadas de ejemplo
conteo_to_limit(10)

print("\nRecorriendo función tradicional:")
for numero in conteo_to_limit(5):
    print("En tradicional", numero)

print("\nRecorriendo generador:")
for numero in conteo_gen(5):
    print("En generador", numero)


