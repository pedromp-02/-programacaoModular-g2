# Módulo de contagem de palavras
from casingComp import *

def gera_matriz_indice(texto):
    i = 0
    palavras = texto.split()
    matriz = []
    usadas = []

    while(i < len(palavras)):
      
      palavras[i] = match_casing("lower", palavras[i]) # match_casing("Title", palavras[i]) ?????
      
      if(palavras[i] not in usadas):
        
        sub_lista = [palavras[i], 1]
        usadas.append(palavras[i])
        matriz.append(sub_lista)
        
      else:
        j = 0
        while compara_palavras(usadas[j], palavras[i]) == 0:
          j += 1
        
        matriz[j][1] += 1 

      i += 1
    
    return matriz # 'texto matriz' falta converter matriz para string
