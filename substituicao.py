# módulo de substituição de palavras em strings

def compara_palavras(palavra1,palavra2):
    palavra1lower = palavra1.casefold()
    palavra2lower = palavra2.casefold()
    return palavra1lower == palavra2lower

def match_casing(palavra1,palavra2):
    if palavra1.isupper(): 
        return palavra2.upper() # upper
    if palavra1.islower():
        return palavra2.lower() # lower
    else:
        if palavra1.istitle():
            return palavra2.title() # title
        else:
            return palavra2.lower() # default

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
