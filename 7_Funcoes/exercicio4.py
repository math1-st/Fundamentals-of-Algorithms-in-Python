a = input("Digite uma palavra: ")

def quantasLetras(a):

    dicionario = {}

    for letra in a:
        
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

    return dicionario

print(quantasLetras(a))