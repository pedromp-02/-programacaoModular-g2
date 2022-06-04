from reutilizaveis.manipulacao import *
from prog1.substituicao import *
from prog2.contagem import *
from prog3.lista_linhas import *

# Testes do Programa 1:
def test_prog1():
    nome_arq = "testando1.txt"
    with open(nome_arq, "w") as f:
        f.write("The usage of certain applications may influence other applications in a positive manner.\n")
    f.close()
    with open(nome_arq, "r") as f:
        texto = gera_string(nome_arq)
    f.close()
    assert substitui_palavra(texto, "applications", "apps") == "The usage of certain apps may influence other apps in a positive manner.\n"

# Testes do Programa 2:
def test_prog2():
    nome_arq = "testando2.txt" 
    with open(nome_arq, "w") as f:
        f.write("This is a test:\nA SIMPLE TEST.\nthis This THIS tHIS!\n234, 4872, 222\né#à@ú")
    f.close()
    with open(nome_arq, "r") as f:
        texto = gera_string(nome_arq)
    f.close()
    esperado = 'This - 5\nIs - 1\nA - 2\nTest - 2\nSimple - 1\n234 - 1\n4872 - 1\n222 - 1\nÉ - 1\nÀ - 3\nÚ - 1\n'
    assert gera_matriz_indice(texto) == esperado
    
