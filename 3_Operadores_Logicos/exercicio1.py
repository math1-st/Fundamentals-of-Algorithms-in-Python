preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print("Procedência = Sul")
elif codigo == 2:
    print("Procedência = Norte")
elif codigo == 3:
    print("Procedência = Leste")
elif codigo == 4:
    print("Procedência = Oeste")
elif codigo >= 5 and codigo <= 6 or codigo >= 25 and codigo <= 30:
    print("Procedência = Nordeste")
elif codigo  == 7 or codigo == 8 or codigo == 9:
    print("Procedência = Sudeste")
elif codigo >= 10 and codigo <= 20:
    print("Procedência = Centro-Oeste")
else:
    print("É importado!")

print(f"Preço: {preco}")
