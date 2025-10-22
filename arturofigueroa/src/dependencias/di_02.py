from abc import ABC, abstractmethod
from dependency_injector import containers, providers

# Interface: defines behavior
class IRepositorioDB(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

# Interface implementation
class RepositorioDB(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Pedido '{pedido}' almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}")

# Business logic
class ServicePedido:
    def __init__(self, repositorio: IRepositorioDB):
        self.repo = repositorio

    def create_order(self, pedido: str):
        print("Mensaje de notificacion")
        print("Impresion de pedido")
        self.repo.guardar(pedido)
        print("Notificacion de almacenaje")

# Dependency injector with pip package
class Contenedor(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioDB)
    service = providers.Factory(ServicePedido, repositorio=repositorio)

# Create container and instance
container = Contenedor()
service_instance = container.service()

# Execute
service_instance.create_order("Pan de muerto")
