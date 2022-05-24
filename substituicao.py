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

#[IMPORTANTE]: Por algum motivo o match_casing nao funciona para ajustar palavras em all caps,
#funciona em aplicacao direta (print(match_casing("HELLO",s))) mas nao em variaveis (word = match_casing(word,s)), trata como uma palavra totalmente miniscula
