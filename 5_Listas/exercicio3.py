l = []

for x in range(1, 11):

    i = int(input("Digite um número: "))
    l.append(i)

maior = l[0]

indice = 0
for y in range(len(l)):

    if maior < l[y]:
        maior = l[y]
        indice = len(l)

print("O maior número é:", maior)
print("O seu indice é", indice)
