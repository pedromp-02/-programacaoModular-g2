# módulo de manipulação de strings e arquivos
import sys

def gera_string(nome_arquivo):
    try:
        f = open(nome_arquivo, "r")
    except:
        sys.exit('Algo deu errado ao tentar abrir o arquivo.')

    text = f.read()
    f.close()
    return text

def gera_arquivo(texto):
    f = open("texto-alterado.txt", "w")
    f.write(texto)
    return
