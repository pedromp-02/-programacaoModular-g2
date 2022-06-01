# módulo que gera uma lista das linhas com a palavra a ser modificada

from casingComp import *
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
                l_aux = [count, s]
                l.append(l_aux)
    return l
  
  
  #[OBS]: Codigo funciona como devido, mas poderia usar mais testes
