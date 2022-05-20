# módulo principal do programa 1
from manipulacao import *
from substituicao import *

'''
abrir arquivo
usar as funcoes dos outros modulos
devolver arquivo modificado
'''
f = open("teste.txt", "w")
con = gera_string(f) # vai gerar uma var string com o conteudo o arquivo
conteudo_final = substitui_palavra(con,"Palavra","PalavraSub")
gera_arquivo(conteudo_final)
