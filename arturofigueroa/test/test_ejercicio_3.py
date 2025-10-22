from arturofigueroa.src.tercerejercicio import RepositorioBD, ServicePedidos
import pytest
from unittest.mock import MagicMock
# Importa tus clases según dónde estén
# from src.dependencias.dic1 import ServicePedidos, RepositorioBD

def test_crear_pedido_llama_a_guardar():
    # Arrange: Creamos el mock del repositorio
    repo_mock = MagicMock(spec=RepositorioBD)
    service = ServicePedidos()
    service.set_repo(repo_mock)
    
    pedido = "Hamburguesita"

    # Act: Llamamos al método que queremos testear
    service.create_order(pedido)

    # Assert: Verificamos que repo_mock.guardar fue llamado exactamente una vez con el pedido correcto
    repo_mock.guardar.assert_called_once_with(pedido)
