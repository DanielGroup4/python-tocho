import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will executing first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Daniel", "Belman", "google.com"]

@pytest.fixture(params=[("chrome", "Dany", "García"), ("Firefox", "Daniel"), ("IE", "Dann")])
def crossBrowser(request):
    return request.param

