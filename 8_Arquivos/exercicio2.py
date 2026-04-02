from random import randint

with open('numeros.txt', 'w') as numeros:
    for _ in range(101):
        numeros.write(f"{randint(1, 1000)} ")

def somar(arquivo):

    with open(arquivo, 'r') as arq_txt:
        dados = arq_txt.read()

    numero = dados.split()

    soma = 0

    for num in numero:
        soma += int(num)

    return soma

resultado = somar('numeros.txt')

print(resultado)