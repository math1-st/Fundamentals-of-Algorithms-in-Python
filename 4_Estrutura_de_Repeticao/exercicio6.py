x = 0
soma = 0
while True:

    print("Digite 0 pra sair.")
    a = int(input("Digite um número: "))

    x = x + 1
    soma = soma + a

    if a == 0:
        print("quantidade de números:", x-1)
        print("soma:", soma)
        print("media:", soma/x)
        break
