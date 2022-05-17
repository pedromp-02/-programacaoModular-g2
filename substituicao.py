# módulo de substituição de palavras em strings

'''
#Prototipo, erros de match_casing a resolver

def replace_word_in_text(txt,w,s):
    x = txt.split(" ")
    word = ""
    aux_word1 = ""
    aux_word2 = ""
    aux_word3 = ""
    t = ""
    counter = 0
    aux_counter = 0
    
    for i in x:
        word = ""
        aux_word = ""
        for c in i:
            if(c == "."):       #Ajuda no detector de caso de "..."
                aux_word1 += c
                aux_counter += 1
                word += c
                
            else:
                word += c

            if(compara_palavras(word,w)):       #Palavra match detectada
                counter = 1
                word = match_casing(word,s)

            elif(aux_counter == 3):     #Caso de "..." confirmado
                aux_word2 += c

                if(aux_word2[1:] == w):
                    counter = 1
                    for a in word:
                        if(a == "."):
                            break
                        aux_word3 += a

                    word = ""
                    word += aux_word3 + aux_word1 + s
                    aux_counter = 0
                    aux_word1 = ""
                    aux_word2 = ""
                    aux_word3 = ""
     
            if(c == " "):       #Break ao terminar a palavra
                aux_word1 = ""
                aux_counter = 0
                break
            
        if(counter == 1):
            t+= " "
            t+=word
            counter = 0
            
        else:
            t+= " "
            t+=i
    return t
'''

def substitui_palavra(texto,palavra_sub):
    return "Teste mock"
