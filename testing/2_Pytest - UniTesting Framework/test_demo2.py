# method name sholud have sense (el nombre del método debe tener sentido)
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# -k representa la ejecución de los nombres de los métodos, -s registra la salida, -v representa más metadatos de información
# you can run specific file with py.test <filename> (puedes ejecutar un archivo específico con py.test <nombre de archivo>)
# you can mark (tag) tests and then run with -m (tu puedes marcar (etiquetar) las pruebas y luego ejecutarlas con -m)
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail

# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixture
# and make it available to all test cases

# las fijaciones se utilizan como métodos de configuración y desmontaje para los casos de prueba -
# archivo conftest para generalizar la fijación y hacerlo disponible para todos los casos de prueba

# datadriven and parametrization can be done with return statements in tuple format
# La parametrización y el control de los datos pueden realizarse con declaraciones de retorno en formato de tupla

# when you define fixture scope to class only, it will run once before class is initiated and at the end
# cuando se define el ámbito del fixture sólo a la clase, se ejecutará una vez antes de que se inicie la clase y al final

import pytest

@pytest.mark.smoke #you can mark (tag) tests and then run with -m
@pytest.mark.skip # you can skip tests with @pytest.mark.skip
def test_firstProgram():
    msg = "Hello" # operation
    assert msg == "Hi", "Test failed becuse strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "addition do not match"

@pytest.fixture()
def setup():
    print("I will be executing first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")