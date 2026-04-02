l = []

for x in range(1, 11):

    i = int(input("Digite um número: "))
    l.append(i)

for y in range(2, len(l)):

    if l[y] > l[y-1] + l[y-2]:
        print(l[y])