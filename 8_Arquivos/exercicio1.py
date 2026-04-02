with open('pares,txt', 'r') as pares, open('invertidos.txt', 'w') as invertidos:
    linhas = pares.readlines()
    for linha in reversed(linhas):
        invertidos.write(linha)