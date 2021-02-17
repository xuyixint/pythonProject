import pytest


@pytest.fixture(scope='session')
def login():
    print("登陆操作》》》》")
    token = datetime.datetime.now()
    yield name
    print("")
