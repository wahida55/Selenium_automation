import pytest
@pytest.fixture()
def setup():
    print("I am setup method...")
    yield
    print("I am done setup...")

def test_fixture(setup):
    print("I am main method...")

@pytest.fixture()
def dataLoad():
    print("User profile is being created!!")
    return ["Wahida","Borbhuyan","wahida55@gmail.com"]

@pytest.fixture(params=[("Chrome","Wahida"),("Firefox","Borbhuyan"),("IE","Right")])
def crossBrowser(request):
    return request.param
