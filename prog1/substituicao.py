# módulo de substituição de palavras em strings
from reutilizaveis.casingComp import *

def substitui_palavra(txt,w,s):
    word = ""
    t = ""
    for c in txt:                               #Pesquisa char por char
        if c.isalpha():               #Verifica se é letra
            word += c
            if compara_palavras(word,w):       #Usa modulo auxiliar para comparacao
                word = match_casing(word,s)     #Usa modulo auxiliar para substituicao
        else:                                   #Constroi palavaras
            t += word
            t += c
            word = ""
    t += word                       # caso termine em letra precisa incluir a palavra final no texto
    word = ""

    return t