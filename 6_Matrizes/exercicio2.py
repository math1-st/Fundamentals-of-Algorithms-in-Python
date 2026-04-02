# Faça um programa que cria uma matriz M 10 X 15, sendo que cada
# elemento é um inteiro gerado aleatoriamente.
# Então, exiba a matriz completa e, na sequência, somente os
# elementos da primeira coluna da matriz
from random import randint

matriz = []

for linha in range(10):

    linha = []
    for coluna in range(15):
        linha.append(randint(1, 100))
    
    matriz.append(linha)

print(matriz)
print()
for linha in range(len(matriz)):
        print(matriz[linha][0])