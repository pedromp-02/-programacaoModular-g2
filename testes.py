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
    
    #assert compara('fine', 'nice') == False
    #assert compara('fine', 'nICE') == False
    #assert compara('fine', 'NICE') == False
    #assert compara('fine', 'Nice') == False
    
    #assert compara('Fine', 'nice') == False
    #assert compara('Fine', 'nICE') == False
    #assert compara('Fine', 'NICE') == False
    #assert compara('Fine', 'Nice') == False
    
    #assert compara('fINE', 'nice') == False
    #assert compara('fINE', 'nICE') == False
    #assert compara('fINE', 'NICE') == False
    #assert compara('fINE', 'Nice') == False
    
    #assert compara('FINE', 'nice') == False
    #assert compara('FINE', 'nICE') == False
    #assert compara('FINE', 'NICE') == False
    #assert compara('FINE', 'Nice') == False
    
def test_casing():
    assert casing('FINE', 'good') == 'GOOD'
    #assert casing('Fine', 'good') == 'Good'
    #assert casing('fINE', 'good') == 'gOOD'
    #assert casing('fine', 'good') == 'good'
  
