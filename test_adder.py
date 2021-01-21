import pytest


def add(x,y):
    return x+y

def test_add():
    total = add(1,1)
    assert total == 2
