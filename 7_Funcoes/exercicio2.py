from random import randint

lista = []
for numeros_aleatorios in range(100):
    lista.append(randint(0, 20))

# ou lista = [randint(0,20) for _ in range(100)]

dicionario = {}

for numero in lista:

    if numero in dicionario:
        dicionario[numero] = dicionario[numero] + 1
    else:
        dicionario[numero] = 1

for key, value in dicionario.items():
    print(f"O número {key} apareceu {value} vezes.")