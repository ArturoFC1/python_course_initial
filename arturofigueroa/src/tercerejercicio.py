# Inyeccion de dependencias por setter

# Clase que almacena el pedido
class RepositorioBD:
    def guardar(self, pedido: str):
        print(f"Pedido '{pedido}' almacenado exitosamente")

# Clase que implementa la lógica de negocio para los pedidos
class ServicePedidos:
    def set_repo(self, repositorio: RepositorioBD):
        # Inicializa la instancia del repositorio
        self.repositorio = repositorio

    def create_order(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repositorio.guardar(pedido)
        print("Notificacion almacenado")

# Inyección de dependencias mediante Setter
repo = RepositorioBD()
service = ServicePedidos()

# Llamada al setter
service.set_repo(repo)

# Llamada al servicio
service.create_order("Hamburguesita")