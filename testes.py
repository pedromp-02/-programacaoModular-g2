from casingComp import *

def comparacao_t1():
    assert test_compara('fine', 'fine') == True
    assert test_compara('fine', 'FINE') == True
    assert test_compara('fine', 'Fine') == True
    assert test_compara('fine', 'fINE') == True
    assert test_compara('fine', 'fiNE') == True
    assert test_compara('fine', 'finE') == True
    assert test_compara('fine', 'fInE') == True
    assert test_compara('fine', 'fINe') == True
    assert test_compara('fine', 'FInE') == True
    assert test_compara('fine', 'FinE') == True    
    assert test_compara('fine', 'FiNE') == True
    assert test_compara('fine', 'FINe') == True
