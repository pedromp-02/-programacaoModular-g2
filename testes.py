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
    
"""
match casing só funciona uppercase, lowercase e titlecase. se não for nenhum desses é
retornado o lowercase. essa aplicação letra a letra só funciona se as palavras terem o
mesmo comprimento, mas elas podem não ter. lembrar de fazer testes para palavras com
comprimentos diferentes.
"""
def test_match_casing():
    assert match_casing('FINE', 'good') == 'GOOD'
    assert match_casing('Fine', 'good') == 'Good'
    #assert match_casing('fINE', 'good') == 'gOOD'
    assert match_casing('fine', 'good') == 'good'
    #assert match_casing('FinE', 'good') == 'GooD'
    #assert match_casing('fiNE', 'good') == 'goOD'
    #assert match_casing('fIne', 'good') == 'gOod'
    #assert match_casing('fINe', 'good') == 'gOOd'
    #assert match_casing('FIne', 'good') == 'GOod'
    #assert match_casing('FiNe', 'good') == 'GoOd'
    #assert match_casing('FInE', 'good') == 'GOoD'
    #assert match_casing('FINe', 'good') == 'GOOd'
  
