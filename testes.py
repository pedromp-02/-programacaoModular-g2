from casingComp import *

def test_comparacao():
    assert compara('fine', 'fine') == True
    assert compara('fine', 'fINE') == True
    assert compara('fine', 'fiNE') == True
    assert compara('fine', 'finE') == True
    assert compara('fine', 'fInE') == True
    assert compara('fine', 'fINe') == True
    assert compara('fine', 'FINE') == True
    assert compara('fine', 'Fine') == True
    assert compara('fine', 'FInE') == True
    assert compara('fine', 'FinE') == True    
    assert compara('fine', 'FiNE') == True
    assert compara('fine', 'FINe') == True
    
    assert compara('Fine', 'fine') == True
    assert compara('Fine', 'fINE') == True
    assert compara('Fine', 'fiNE') == True
    assert compara('Fine', 'finE') == True
    assert compara('Fine', 'fInE') == True
    assert compara('Fine', 'fINe') == True
    assert compara('Fine', 'FINE') == True
    assert compara('Fine', 'Fine') == True
    assert compara('Fine', 'FInE') == True
    assert compara('Fine', 'FinE') == True    
    assert compara('Fine', 'FiNE') == True
    assert compara('Fine', 'FINe') == True
