import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [(1, 2), (10, 20), ('a', 'a1')])
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5

    def login():
        print("登陆操作")
        username = 'Jerry'
        return username


class TestDemo:
    def test_a(self):
        print(f"a  username={login}")

    def test_b(self):
        print("b")

    def test_c(self):
        print(f"c")


if __name__ == '_main_':
    pytest.main(['test_a.py::TestDemo', '-v'])
