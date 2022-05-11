from casingComp import *

def test_comparacao():
    assert compara('fine', 'fine') == True
    assert compara('fine', 'Fine') == True
    assert compara('fine', 'FINE') == True
    assert compara('fine', 'fINE') == True
    
    assert compara('Fine', 'fine') == True
    assert compara('Fine', 'Fine') == True
    assert compara('Fine', 'FINE') == True
    assert compara('Fine', 'fINE') == True
    
    assert compara('FINE', 'fine') == True
    assert compara('FINE', 'Fine') == True
    assert compara('FINE', 'FINE') == True
    assert compara('FINE', 'fINE') == True
    
    assert compara('fINE', 'fine') == True
    assert compara('fINE', 'Fine') == True
    assert compara('fINE', 'FINE') == True
    assert compara('fINE', 'fINE') == True
    
 def test_casing():
    assert casing('FINE', 'good') == 'GOOD'
    #assert casing('Fine', 'good') == 'Good'
    #assert casing('fINE', 'good') == 'gOOD'
    #assert casing('fine', 'good') == 'good'
  
