# Um cartão de bingo consiste de 5 colunas de 5 números. As
# colunas são rotuladas com as letras B, I, N, G e O. Existem 15
# números que podem aparecer na coluna de cada letra. Em
# particular, os números que podem aparecer na coluna de B estão
# no intervalo de 1 a 15, os números que podem aparecer sob o I
# variam de 16 a 30 e assim por diante. Escreva uma função que
# cria um cartão de Bingo com números aleatórios e armazena tudo
# em um dicionário. As chaves serão as letras B, I, N, G e O.
# Os valores serão as listas de cinco números que aparecem em
# cada letra.

# For each letter, there will be 15 random numbers between x-y
# Create a bingo card with five column

from random import randint

def criarBingo():

    i = 15
    g = 1

    for chave in dicionario.keys():

        for vezes in range(5):

            dicionario[chave].append(randint(g, i))

        i += 15
        g += 15

    return dicionario

dicionario = {
    'B': [],
    'I': [],
    'N': [],
    'G': [],
    'O': []
}

for key, value in criarBingo().items():
    print(f"{key}: {value}")