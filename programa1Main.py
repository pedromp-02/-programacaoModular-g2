# módulo principal do programa 1
from manipulacao import *
from substituicao import *

'''
abrir arquivo
usar as funcoes dos outros modulos
devolver arquivo modificado
'''
print('Bem vindo ao programa de substituição de palavras.')
if input('Digite "h" caso queira ver o guia de uso, qualquer outra tecla para prosseguir para o programa: ') == 'h':
    print('O programa irá pedir o nome de um arquivo em que a substituição irá acontecer.')
    print('Inclua o formato, como por exemplo "arquivo.txt" em vez de somente "arquivo".')
    print('Caso o arquivo não esteja no diretório do programa, especifique seu caminho inteiro (como "C:\\Users\\User\\Desktop\\arquivo.txt").')
    print('Então, o programa irá pedir duas palavras:')
    print(' - A primeira será substituída no arquivo origem')
    print(' - A segunda será sua substituição')

nome_arquivo = input('Entre com o arquivo (incluindo formato): ')
texto = gera_string(nome_arquivo)

palavra = input('Entre com a palavra a ser substituída: ')
while (palavra.isalpha() == False):
    palavra = input('Palavra inválida. Tente novamente: ')

sub = input('Entre com a substituição: ')
while (sub.isalpha() == False):
    sub = input('Palavra inválida. Tente novamente: ')

conteudo_final = substitui_palavra(texto,palavra,sub)

dir = input('Entre com o nome do arquivo a ser salvo, com formato (diretório para salvar em outra pasta): ')
gera_arquivo(conteudo_final, dir)

print('Arquivo gerado.')

input('Enter para sair')
