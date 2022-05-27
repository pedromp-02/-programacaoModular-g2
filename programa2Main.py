# módulo principal do programa 2
from manipulacao import *
from contagem import *

'''
abrir arquivo
usar as funcoes dos outros modulos
devolver arquivo modificado
'''
print('Bem vindo ao programa de contagem de palavras.')
if input('Digite "h" caso queira ver o guia de uso, qualquer outra tecla para prosseguir para o programa: ') == 'h':
    print('O programa irá pedir o nome de um arquivo para contar as palavras.')
    print('Inclua o formato, como por exemplo "arquivo.txt" em vez de somente "arquivo".')
    print('O arquivo deve estar no mesmo diretório do programa.')
    print('Então, o programa irá contar a quantidade de ocorrências de cada palavra no arquivo.')
    print('A saída será printada na tela.')
    print('Será dada a opção de gerar um arquivo com a contagem de saída.')

nome_arquivo = input('Entre com o nome do arquivo (incluindo formato): ')
texto = gera_string(nome_arquivo)

conteudo_final = gera_matriz_indice(texto)
print("Contagem: ")
print(conteudo_final)

if input("Para gerar arquivo com a saída, digite 'Y': ").lower() == 'y':
    gera_arquivo(conteudo_final)
    print('Arquivo gerado.')

exit()
