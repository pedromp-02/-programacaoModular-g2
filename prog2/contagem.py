# Módulo de contagem de palavras
# dependências: módulo reutilizável casingComp
from reutilizaveis.casingComp import *
import re 

def gera_matriz_indice(texto):
    i = 0 # contador do while
    palavras = re.findall(r'\w+', texto) # transforma o texto em um array de suas palavras
    matriz = [] # matriz para montar o índice de contagem
    usadas = [] # lista de palavras que já estão na matriz

    while(i < len(palavras)): # checa cada palavra do texto
      
      palavras[i] = match_casing("Title", palavras[i]) # coloca palavra em Title Case

      if(palavras[i] not in usadas): # se não estiver na matriz

        sub_lista = [palavras[i], 1]
        usadas.append(palavras[i])
        matriz.append(sub_lista)
        # coloca na lista de usadas e coloca seu contador na matriz

      else: # se estiver
        j = 0
        while compara_palavras(usadas[j], palavras[i]) == False: # encontra sua posição
          j +=1
        
        matriz[j][1] += 1 # adiciona 1 ao seu contador

      i+=1

    i = 0
    string = "" # texto que será retornado
    while(i < len(usadas)):
      string += f'{matriz[i][0]} - {matriz[i][1]}\n' # monta cada linha do texto
      i += 1
    
    return string
