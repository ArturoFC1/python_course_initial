"Inyeccion por dependencias por constructor"
"""""
#Clase que almacena pedido
class RepositorioBD:
    def guardar(self, pedido: str):
        print(f"Pedido {pedido} almacenado exitosamnete")

#Clase que implementa logica del pedido
class ServicePedidos:
    def __init__(self, repositorio: RepositorioBD):
        self.repositorio = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repositorio.guardar(pedido)
        print("Notificacion de almacenado")

#Inyeccion de dependencias por constructor
repo = RepositorioBD()
service = ServicePedidos(repo)

#LLama a serviicos

service.crear_pedido("Gamburguesa")

////////////////////////////////////////////////////////////////////////////////////////////////////77

#Interfazes como patrones
from abc import ABC, abstractmethod

class IRepositorioDB(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioDB(IRepositorioDB):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamnete")

class ServicePedido:
    def __init__(self, repositorio: IRepositorioDB):
        self.repo = repositorio

    def crear_pedido(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion por orden")
        self.repo.guardar(pedido)
        print("Notificacion almacenado")

repoDB: IRepositorioDB = RepositorioDB()

service = ServicePedido(repoDB)

service.crear_pedido("Tacos")

/////////////////////////////////////////////////////////

"""

# Dependency Injection by Setter

# Class that stores the order
class RepositorioBD:
    def guardar(self, pedido: str):
        print(f"Pedido '{pedido}' almacenado exitosamente")

# Class that implements business logic for the order
class ServicePedidos:
    def set_repo(self, repositorio: RepositorioBD):
        # Initializes the instance of the repository
        self.repositorio = repositorio

    def create_order(self, pedido: str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repositorio.guardar(pedido)
        print("Notificacion almacenado")

# Dependency Injection by Setter
repo = RepositorioBD()
service = ServicePedidos()

# Call to the setter
service.set_repo(repo)

# Call to the service
service.create_order("Hamburguesita")



#Inyeccion manual de dependecias
"""""""""""
class Container:
    def __init__(self):
        self._servicios = {}

    def register(self, nombre, creator):
        self._servicios[nombre] = creator

    def resolver(self, nombre):
        return self._servicios[nombre]()

container = Container()
container.register("repositorio", lambda: ApiTercerosAdapter())

"""""