# Módulo de contagem de palavras
from reutilizaveis.casingComp import *
import re 

def gera_matriz_indice(texto):
    i = 0
    cont = 0
    palavras = re.findall(r'\w+', texto)
    matriz = []
    usadas = []
    string = ""

    while(i < len(palavras)):
      
      palavras[i] = match_casing("Title", palavras[i])

      if(palavras[i] not in usadas):

        sub_lista = [palavras[i], 1]
        usadas.append(palavras[i])
        matriz.append(sub_lista)
        
      else:
        j = 0
        while compara_palavras(usadas[j], palavras[i]) == 0:
          j +=1
        
        matriz[j][1] += 1
        cont += 1

      i+=1

    i = 0
    while(i < cont):
      string += f'{matriz[i][0]} - {matriz[i][1]}\n'
      i += 1
    
    return string
