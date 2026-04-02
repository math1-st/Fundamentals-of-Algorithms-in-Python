# Faça um programa que cria um matriz A 10 X 5 com números
# inteiros aleatórios e, então, exiba a matriz transposta de
# A(At)
# Determinar a transposta de uma matriz é reescrevê-la de forma
# que suas linhas e colunas troquem de posições ordenadamente,
# isto é, a primeira linha é reescrita como a primeira coluna, a
# segunda linha é reescrita como a segunda coluna e assim por
# diante, até que se termine de reescrever todas as linhas na
# forma de coluna.

from random import randint

matriz = []

for linha in range(10):
    linha = []
    for coluna in range(5):
        linha.append(randint(1, 100))
    matriz.append(linha)

print("Matriz:")
for linha in matriz:
    print(linha)

matriz_transposta = []
for t_coluna in range(5):
    linha = []
    for t_linha in range(10):
        linha.append(matriz[t_linha][t_coluna])
    matriz_transposta.append(linha)

print("\nMatriz Transposta:")
for linha  in matriz_transposta:
    print(linha)