distancia = int(input("Digite a distância: "))

if distancia <= 200:
    preco = distancia * 0.5
    print(preco)
else:
    preco = distancia * 0,45
    print(preco)