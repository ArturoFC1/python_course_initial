# Clase simple sin setter
class Producto:
    'Clase producto. Propiedades de un producto'
    def __init__(self, nombre: str, precio: float ):
        'Constructor de clase'
        self.nombre = nombre
        self.precio = precio

# Creamos una instancia
producto_uno = Producto("Pan", 30)
print(f"Producto 1: {producto_uno.nombre} costo de {producto_uno.precio}")

# --------------------------------------------

# Clase con @property y setter
class ProductoSetter:
    'Clase producto, propiedades de un producto'

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio  # llama al setter automáticamente

    @property
    def precio(self) -> float:
        'Getter, permite acceder a la propiedad .precio'
        return self._precio
    
    @precio.setter
    def precio(self, value: float):
        'Setter, permite modificar el precio y aplicar validaciones'
        if value <= 0:
            raise ValueError("El precio debe de ser mayor a cero")
        self._precio = value

    def __str__(self):
        "Metodo especial que nos permite el llamdo para convertir a cadena de texto"
        return f"---El producto {self.nombre} tiene un costo de {self.precio}"


# Instanciamos fuera de la clase
producto_dos = ProductoSetter("Pan linaza", 32)
print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")

# Modificamos el precio usando el setter
producto_dos.precio = 89
print(f"Producto 2: {producto_dos.nombre} costo de {producto_dos.precio}")

