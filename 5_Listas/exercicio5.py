# Slicing -> [::]
# Slicing pode pegar de qualquer ponto, de qualquer direção.
# [:] permite fazer a cópia corretamente de uma lista sem alterar a lista original.

l = []

vezes = int(input("Digite quantas vezes: "))
for x in range(1, vezes+1):

    i = int(input("Digite um número: "))
    l.append(i)

lx = l[::-1]
print("Lista Normal:", l)
print("Lista Invertida:", lx)

for x in lx:
    print(x)