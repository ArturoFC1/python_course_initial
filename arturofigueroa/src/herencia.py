class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado (Persona):
    def __init__(self, nombre, puesto):
        super().__init__(nombre)
        self.puesto = puesto

    def __str__(self): #Como un tostring
        return f"Empleado {self.nombre}"

empleado = Empleado("Arturo", "Trainee")
print(empleado)