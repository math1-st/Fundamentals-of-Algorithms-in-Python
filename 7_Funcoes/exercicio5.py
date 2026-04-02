a = input("Digite a primeira palavra: ")
b = input("Digite a segunda palavra: ")

def eh_anagrama(palavra):

    dicionario = {}

    for letra in palavra:
        
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

    return dicionario

primeira_palavra = eh_anagrama(a)
segunda_palavra = eh_anagrama(b)

if primeira_palavra == segunda_palavra:
    print(f"{a} e {b} são anagramas.")
else:
    print(f"{a} e {b} NÃO são anagramas.")