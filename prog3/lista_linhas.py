# módulo que gera uma lista das linhas com a palavra a ser modificada
# dependências: módulo reutilizável casingComp
from reutilizaveis.casingComp import *
import re

#Funcao geradora da lista de linhas l = [[num_linha, linha referente], ...]
def gera_lista_linhas(texto, palavra):
    l = []
    l_aux = []
    count = 0
    
    txt = texto.split('\n')                         #Divide o texto em linhas
    for s in txt:                                   #Navega linha por linha
        count += 1                                  #Mantem o numero da linha
        line = re.findall(r'\w+', s)                #Separa as palavras da linha ignorando sua pontuacao
        for w in line:                              #Analisa palavra por palavra
            if compara_palavras(w,palavra):         #Verifica a palavra usando o modulo casingComp
                if len(l) < 1 or l[-1][0] != count: #Adiciona somente se a linha não já estiver adicionada
                    l_aux = [count, s]
                    l.append(l_aux)
    
    text = ""
    for linha in l:
        text += f"{linha[0]} - {linha[1]}\n" # monta o texto a partir da lista

    return text
