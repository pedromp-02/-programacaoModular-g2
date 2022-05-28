from substituicao import *

# Testes do módulo de substituição de palavras:
def test_substitui_palavra():
    assert substitui_palavra('a string', 'a', 'another') == 'another string'
    assert substitui_palavra('EXAMPLE', 'EXAMPLE', 'TEST') == 'TEST'
    assert substitui_palavra('Small test', 'small', 'big') == 'Big test'
    assert substitui_palavra('hello world', 'HELLO', 'hi') == 'hi world'
    assert substitui_palavra('This is sPECIFIC', 'SpeCiFiC', 'nEAT') == 'This is neat'
    assert substitui_palavra('The following word is deleted', 'DELETED', '') == 'The following word is '
    assert substitui_palavra('There are 365 days in a year.', '365', '999') == 'There are 365 days in a year.'
    assert substitui_palavra('Make it wORK', 'work', 'rUN') == 'Make it run'
    assert substitui_palavra('Have a good DaY', 'DAY', 'EVENING') == 'Have a good evening'
    assert substitui_palavra('This is clearly a test', 'cLEARLY', 'simply') == 'This is simply a test'
    
# Testes do programa 1:
