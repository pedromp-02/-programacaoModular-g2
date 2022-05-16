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
    assert match_casing('I', 'i') == 'I'
    assert match_casing('i', 'i') == 'i' 
    
    assert match_casing('I', 'am') == 'AM'
    assert match_casing('i', 'am') == 'am' 
    
    assert match_casing('HE', 'my') == 'MY'
    assert match_casing('He', 'my') == 'My' 
    assert match_casing('he', 'my') == 'my'
    
    assert match_casing('HI', 'hello') == 'HELLO'
    assert match_casing('Hi', 'hello') == 'Hello' 
    assert match_casing('hi', 'hello') == 'hello'
    
    assert match_casing('TRY', 'dry') == 'DRY'
    assert match_casing('Try', 'dry') == 'Dry'
    assert match_casing('try', 'dry') == 'dry'
    
    assert match_casing('WHY', 'where') == 'WHERE'
    assert match_casing('Why', 'where') == 'Where'
    assert match_casing('why', 'where') == 'where'
    
    assert match_casing('FINE', 'good') == 'GOOD'
    assert match_casing('Fine', 'good') == 'Good'
    assert match_casing('fine', 'good') == 'good'
   
    assert match_casing('SOUP', 'vegetable') == 'VEGETABLE'
    assert match_casing('Soup', 'vegetable') == 'Vegetable'
    assert match_casing('soup', 'vegetable') == 'vegetable'
    
    assert match_casing('LIGHT', 'heavy') == 'HEAVY'
    assert match_casing('Light', 'heavy') == 'Heavy'
    assert match_casing('light', 'heavy') == 'heavy'
    
    assert match_casing('RANCH', 'hyperbole') == 'HYPERBOLE'
    assert match_casing('Ranch', 'hyperbole') == 'Hyperbole'
    assert match_casing('ranch', 'hyperbole') == 'hyperbole'
    
    assert match_casing('HEIGHT', 'crouch') == 'CROUCH'
    assert match_casing('Height', 'crouch') == 'Crouch'
    assert match_casing('height', 'crouch') == 'crouch'
    
    assert match_casing('MIGHTY', 'henceforth') == 'HENCEFORTH'
    assert match_casing('Mighty', 'henceforth') == 'Henceforth'
    assert match_casing('mighty', 'henceforth') == 'henceforth'
    
    #assert match_casing('fINE', 'good') == 'good'    
    #assert match_casing('FinE', 'good') == 'good'
    #assert match_casing('fiNE', 'good') == 'good'
    #assert match_casing('fIne', 'good') == 'good'
    #assert match_casing('fINe', 'good') == 'good'
    #assert match_casing('FIne', 'good') == 'good'
    #assert match_casing('FiNe', 'good') == 'good'
    #assert match_casing('FInE', 'good') == 'good'
    #assert match_casing('FINe', 'good') == 'good'
  
    
