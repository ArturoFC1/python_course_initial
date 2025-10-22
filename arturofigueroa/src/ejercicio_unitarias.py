class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def validar_email(self) -> bool:
        "Valida estructura de correo"
        return "@" in self.correo and "." in self.correo
    
    
cliente = Cliente("Arturo", "co@r.reo")

print(cliente.validar_email())
