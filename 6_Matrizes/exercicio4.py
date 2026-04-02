# Solicitar dados de uma matriz 4 X 4
# Montar uma lista de 4 elementos com a soma dos elementos
# ímpares de cada linha da matriz

matriz = []

for linha in range(4):
    linha = []
    for coluna in range(4):
        numero = int(input("Digite um inteiro: "))
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    print(linha)

lista_soma_impares = []
for linha in matriz:
    soma_impares = 0
    for coluna in linha:
        if coluna % 2 != 0:
            soma_impares += coluna
    lista_soma_impares.append(soma_impares)

print(lista_soma_impares)