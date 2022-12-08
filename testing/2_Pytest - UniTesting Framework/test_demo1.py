# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only (cualquier código debe ser envuelto en un método solamente)
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail # py.test -v -s
def test_secondGreetCreditCard():
    print("Good night")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])