from arturofigueroa.src.ejercicio_unitarias import Cliente

def test_validar_email_succes():
    #Arrange
    email_valido = "emailtest.com"

    #Llamada

    cliente_test = Cliente("Jona",email_valido)

    #Asssert

    assert cliente_test.validar_email() is True