# módulo de manipulação de strings e arquivos
import sys

def gera_string(nome_arquivo):
    try:
        f = open(nome_arquivo, "r", encoding="utf-8")
    except:
        sys.exit('Algo deu errado ao tentar abrir o arquivo.')

    text = f.read()
    f.close()
    return text

def gera_arquivo(texto, dir):
    try:
        f = open(dir, "w")
    except:
        sys.exit('Algo deu errado ao tentar escrever.')

    f.write(texto)
    f.close()
    return
