from casingComp import *

def test_comparacao():
    assert compara('fine', 'fine') == True
    assert compara('fine', 'FINE') == True
    assert compara('fine', 'Fine') == True
    assert compara('fine', 'fINE') == True
    assert compara('fine', 'fiNE') == True
    assert compara('fine', 'finE') == True
    assert compara('fine', 'fInE') == True
    assert compara('fine', 'fINe') == True
    assert compara('fine', 'FInE') == True
    assert compara('fine', 'FinE') == True    
    assert compara('fine', 'FiNE') == True
    assert compara('fine', 'FINe') == False
