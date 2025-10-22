"""""
    Simular calculo del precio final del profucto con IVA     

"""""
precio_producto = 400
porcentaje_iva = 16

def calcular_iva(precio_producto, porcentaje_iva):
    calculo_porciento = porcentaje_iva * 0.01

    return calculo_porciento * precio_producto

def calcular_precio_final():
    precio_final = precio_producto + calcular_iva(precio_producto, porcentaje_iva)
    return precio_final

print(f"El precio final es {calcular_precio_final()}")