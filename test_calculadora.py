from calculadora import * 

def test_sumar():
    assert sumar(2,3) == 5 

def test_restar():
    assert restar(5,2) == 3
    
def test_multi():
    assert multi(3,2) == 6 
    
def test_divi():
    assert divi(4,2) == 2
    