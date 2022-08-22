import pytest

def fun(num):
    for i in range(2,num):
        if num%2 == 0:
            print('not prime')
            break
    else:
        return 'prime'

def test_Prime():
    n = 7
    assert fun(n)=='prime'

pytest.main()