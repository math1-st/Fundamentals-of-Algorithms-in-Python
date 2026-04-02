# Matrizes
# Exercício 01
# Crie 3 listas:
# ▶ Inteiros: a primeira lista com 10 números inteiros gerados
# aleatoriamente
# ▶ Reais: a segunda lista com 5 números reais gerados
# aleatoriamente
# ▶ Strings: A terceira lista com 7 strings criadas por você.
# Então adicione as 3 listas a uma lista única, chamada
# completa.
# Apague todas as 3 listas originais.
# Acesse e mostre todos os elementos da lista completa.

from random import randint, random

matriz = []

dez_inteiros = [randint(1, 100) for _ in range(10)]

cinco_reais = [random() * 100 for _ in range(5)]

sete_strings = ['q', 'w', 'e', 'r', 't', 'y', 'u']

matriz.append(dez_inteiros)
matriz.append(cinco_reais)
matriz.append(sete_strings)

del dez_inteiros
del cinco_reais
del sete_strings

print(matriz)

# matriz.append()