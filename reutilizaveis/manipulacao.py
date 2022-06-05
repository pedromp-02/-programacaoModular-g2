# módulo de manipulação de strings e arquivos
import sys

def gera_string(nome_arquivo):
    try: # tenta abrir o arquivo
        f = open(nome_arquivo, "r")
    except: # caso não encontre ou outro erro na abertura
        sys.exit('Algo deu errado ao tentar abrir o arquivo.')

    text = f.read() # transforma o arquivo em string
    f.close()   # fecha arquivo
    return text # retorna texto do arquivo

def gera_arquivo(texto, dir):
    try: # tenta abrir/criar o arquivo
        f = open(dir, "w")
    except: # caso não consiga abrir/criar
        sys.exit('Algo deu errado ao tentar escrever.')

    f.write(texto)  # escreve o texto recebido no arquivo
    f.close()   # fecha o arquivo de escrita
    return
