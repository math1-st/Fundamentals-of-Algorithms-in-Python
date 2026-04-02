matriz = []

for linha in range(3):
    linha = []
    for coluna in range(3):
        numero = int(input("Digite um inteiro: "))
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    print(linha, "\n", end='')

soma_diagonal_principal = 0
for i in range(len(matriz)):
    soma_diagonal_principal += matriz[i][i]
    
print(soma_diagonal_principal)