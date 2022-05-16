from casingComp import *
from manipulacao import *

def test_compara_palavrascao():
    assert compara_palavras('fine', 'fine') == True
    assert compara_palavras('fine', 'Fine') == True
    assert compara_palavras('fine', 'FINE') == True
    assert compara_palavras('fine', 'fINE') == True
    
    assert compara_palavras('Fine', 'fine') == True
    assert compara_palavras('Fine', 'Fine') == True
    assert compara_palavras('Fine', 'FINE') == True
    assert compara_palavras('Fine', 'fINE') == True
    
    assert compara_palavras('FINE', 'fine') == True
    assert compara_palavras('FINE', 'Fine') == True
    assert compara_palavras('FINE', 'FINE') == True
    assert compara_palavras('FINE', 'fINE') == True
    
    assert compara_palavras('fINE', 'fine') == True
    assert compara_palavras('fINE', 'Fine') == True
    assert compara_palavras('fINE', 'FINE') == True
    assert compara_palavras('fINE', 'fINE') == True
    
    assert compara_palavras('fine', 'nice') == False
    assert compara_palavras('fine', 'nICE') == False
    assert compara_palavras('fine', 'NICE') == False
    assert compara_palavras('fine', 'Nice') == False
    
    assert compara_palavras('Fine', 'nice') == False
    assert compara_palavras('Fine', 'nICE') == False
    assert compara_palavras('Fine', 'NICE') == False
    assert compara_palavras('Fine', 'Nice') == False
    
    assert compara_palavras('fINE', 'nice') == False
    assert compara_palavras('fINE', 'nICE') == False
    assert compara_palavras('fINE', 'NICE') == False
    assert compara_palavras('fINE', 'Nice') == False
    
    assert compara_palavras('FINE', 'nice') == False
    assert compara_palavras('FINE', 'nICE') == False
    assert compara_palavras('FINE', 'NICE') == False
    assert compara_palavras('FINE', 'Nice') == False
    
def test_match_casing():
    assert match_casing('FINE', 'good') == 'GOOD'
    assert match_casing('Fine', 'good') == 'Good'
    assert match_casing('fine', 'good') == 'good'
    assert match_casing('fINE', 'good') == 'good'
    
