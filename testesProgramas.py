from reutilizaveis.manipulacao import *
from prog1.substituicao import *

# Testes do Programa 1:
def test_prog1():
    nome_arq = "testando.txt"
    with open(nome_arq, "w") as f:
        f.write("The usage of certain applications may influence other applications in a positive manner.\n")
    f.close()
    with open(nome_arq, "r") as f:
        texto = gera_string(nome_arq)
    f.close()
    assert substitui_palavra(texto, "applications", "apps") == "The usage of certain apps may influence other apps in a positive manner.\n"
