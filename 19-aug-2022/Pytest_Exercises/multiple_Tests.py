import pytest

def test_case():
    a = 5
    b = 6
    assert a+b == 11

def test_case2():
    n = 8
    m = 8
    assert n is m

def test_case3():
    h = 9 
    n = 4
    assert h*n==36


pytest.main()
