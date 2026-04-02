nascimento = int(input("Em que ano você nasceu: "))

idade = 2025 - nascimento
print(idade)

if idade >= 18:
    print("Você já tem idade para tirar CNH.")
else:
    print("Não tem idade para dirigir.")

if idade >= 16:
    print("Já pode votar.")
else:
    print("Não pode votar.")