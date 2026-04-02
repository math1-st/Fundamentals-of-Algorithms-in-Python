codigo = int(input("Digite o código de um produto: "))

if codigo == 1:
    print("Alimento não perecível.")
elif codigo >= 2 and codigo <= 4:
    print("Alimento perecível.")
elif codigo == 5 or codigo == 6:
    print("Vestuário.")
elif codigo == 7:
    print("Higiene pessoal.")
elif codigo >= 8 and codigo <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido.")