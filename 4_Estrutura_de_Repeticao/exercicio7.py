x = 0
soma = 0

while x < 10:
    x = x + 1
    a = int(input("Descubra a soma de dez números: "))
    soma = soma + a
    print(f"{x}º contagem.")
    print("Soma:", soma)