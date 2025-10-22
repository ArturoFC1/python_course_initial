# args

#Argumentos posicionales
def procesar_datos(*args) -> None:
    'Recibe argumentos posicionales'
    print(f"Argumentos: {args}")

#key arguments
def procesar_datos_kw(**kwargs) -> None:
    'Recibe argumentos posicionales'
    print(f"Argumentos: {kwargs}")


procesar_datos(1,3,4,5,6,7,4,3)
procesar_datos_kw(nombre = "Arturo", status=True)