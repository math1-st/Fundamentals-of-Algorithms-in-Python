l = []

for x in range(1, 11):

    i = int(input("Digite um número: "))
    l.append(i)

soma_par = 0
i = 0
soma_indice_par = 0
for y in l:

    if y % 2 == 0:
        soma_par += y
    
    if i % 2 == 0:
        soma_indice_par += y
    
    i += 1

print("Soma dos números pares:", soma_par)
print("Soma dos números de indices pares:", soma_indice_par)
