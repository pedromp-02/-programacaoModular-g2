# módulo de comparação e casing match

# compara as duas palavras em minúsculo, retorna o resultado da comparação
def compara_palavras(palavra1,palavra2):
    palavra1lower = palavra1.casefold()
    palavra2lower = palavra2.casefold()
    return palavra1lower == palavra2lower

"""
três casos:
- tudo maiúsculo
- tudo minúsculo
- title case
se a palavra não for nenhum dos casos defaulta pra minúsculo
"""
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
