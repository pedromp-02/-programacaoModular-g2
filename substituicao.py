# módulo de substituição de palavras em strings

def substitui_palavra(txt,w,s):
    word = ""
    t = ""
    for c in txt:                               #Pesquisa char por char
        if(c == ' ' or c == '.'):               #Verificador para o timing de adicionamento para to texto resultado
            t += word
            t += c
            word = ""
            
        else:                                   #Constroi palavaras
            word += c
            if(compara_palavras(word,w)):       #Usa modulo auxiliar para comparacao
                word = match_casing(word,s)     #Usa modulo auxiliar para substituicao
            
    return t
