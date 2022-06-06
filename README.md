
# INF1301 - Grupo 2
### Repositório feito para o trabalho de **Programação Modular 2022.1**
*Integrantes:*
- Guilherme Carreira Marques
- Guilherme Ricardo Rezende Gomes
- Igor Soares Lemos
- João Pedro Sande de Souza
- João Quintella do Couto
- João Roizen Fontana
- Luca Vasconcellos Ribeiro
- Patrick Utzig Haselof

## Instruções de uso
**Gerais**: 
- Todos os programas operam em arquivos texto. Caso o arquivo texto esteja no mesmo diretório do programa, basta seu nome com o formato (como *arquivo.txt*).
Caso o arquivo não esteja no diretório do programa, especifique seu caminho inteiro (como *C:\\Users\\User\\Desktop\\arquivo.txt*)
- Qualquer comparação que os programas fazem ignoram o *casing* das palavras, ou seja, 'palavra', 'Palavra' e 'PALAVRA' são iguais. 

### Programa 1
O programa 1 é um programa de substituição de palavras em arquivos texto.
O programa irá pedir o nome de um arquivo em que a substituição irá acontecer. Esse input deve ser da forma especificada nas instruções gerais.

Então, o programa irá pedir duas palavras:
- A primeira será a palavra a ser substituída no arquivo origem.
- A segunda será a substituição utilizada.

A substituição é feita levando em conta o *casing* da palavra a ser substituída. Existem três casos de *casing* considerados: UPPERCASE, Titlecase, lowercase. Caso o casing não seja um desses três, o *casing* utilizado será lowercase. 

**EXEMPLO:**
Caso o programa substitua palavra 'teste' pela palavra 'prova' no arquivo abaixo:
>TESTE Teste teste tEstE

A saída será da forma:
>PROVA Prova prova prova

### Programa 2
O programa 2 é um programa de contagem de palavras.
O programa irá pedir o nome de um arquivo em que a substituição irá acontecer. Esse input deve ser da forma especificada nas instruções gerais.

Então, o programa irá contar as ocorrências de cada uma das palavras utilizadas no texto. O programa mostra o resultado e dá a opção de se salvar o resultado em um arquivo.

**EXEMPLO:**
Caso o programa realize a contagem no arquivo abaixo:


A saída será da forma:

>Arquivo - 2

>De - 2

>Teste - 3

>Esse - 1

>É - 1

>Um - 1

>Se - 1

>Funciona - 1

### Programa 3
O programa 3 é um programa de listagem de linhas.
O programa irá pedir o nome de um arquivo para realizar a listagem. Esse input deve ser da forma especificada nas instruções gerais.

Então, o programa irá pedir uma palavra para o qual a listagem será feita.

O programa registra cada linha que a palavra ocorre e sua posição, de forma que a saída tenha todas as linhas em que a palavra ocorre. Cada linha é registrada no máximo uma vez, mesmo que contenha múltiplas ocorrências da palavra a registrar.

**EXEMPLO:**
Caso o programa realize a listagem da palavra 'teste' no arquivo abaixo:

>Arquivo de teste.

>Esse é um arquivo de teste. Essa linha contém teste duas vezes.

>Essa linha não contém a palavra.

>Teste se funciona.

>Essa linha também não.


A saída será da forma:

>1 - Arquivo de teste.

>2 - Esse é um arquivo de teste. Essa linha contém teste duas vezes.

>4 - Teste se funciona.
