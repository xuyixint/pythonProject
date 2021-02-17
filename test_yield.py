import pytest


@pytest.fixture(params=['hali', 'haomin'])


def login():
    print('login')
