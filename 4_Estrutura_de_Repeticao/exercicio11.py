qnt_habitantes = 5

soma_idade_homem = 0
soma_idade_mulher = 0

qnt_genero_m = 0
qnt_genero_f = 0

soma_salario_homem = 0
soma_salario_mulher = 0

x = 0
while x < qnt_habitantes:

    x = x + 1

    ask_genero = input("Você se identifica como M ou F: ")

    if ask_genero == "M" or ask_genero == "m":

        qnt_genero_m = qnt_genero_m + 1

        ask_idade_homem = int(input("[M] - Qual a sua idade: "))

        if ask_idade_homem <= 0:
            print("Por favor, digite uma idade válida.")
            break
        else:
            soma_idade_homem = soma_idade_homem + ask_idade_homem

        if ask_idade_homem >= 16:
            ask_salario_homem = float(input("[M] - Qual o seu salário: "))
            soma_salario_homem = soma_salario_homem + ask_salario_homem
        else:
            soma_salario_homem = soma_salario_homem + 0

    elif ask_genero == "F" or ask_genero == "f":

        qnt_genero_f = qnt_genero_f + 1
        ask_idade_mulher = int(input("[F] - Qual a sua idade: "))

        if ask_idade_mulher <= 0:
            print("Por favor, digite uma idade válida.")
            break
        else:
            soma_idade_mulher = soma_idade_mulher + ask_idade_mulher

        if ask_idade_mulher >= 16:
            ask_salario_mulher = float(input("[F] - Qual o seu salário: "))
            soma_salario_mulher = soma_salario_mulher + ask_salario_mulher
        else:
            soma_salario_mulher = soma_salario_mulher + 0
            
    else:
        print("Digite corretamente!")
        x = x - 1

soma_idade = soma_idade_homem + soma_idade_mulher
soma_salarial = soma_salario_homem + soma_salario_mulher

media_idade = soma_idade / x
media_salarial = soma_salarial / x

idade_media_masculina = soma_idade_homem / qnt_genero_m
idade_media_feminina = soma_idade_mulher / qnt_genero_f

media_salarial_masculina = soma_salario_homem / qnt_genero_m
media_salarial_feminina = soma_salario_mulher / qnt_genero_m

print(f"\nForam entrevistados {qnt_genero_m} homens e {qnt_genero_f} mulheres.\n")

print(f"Media de idade geral é: {media_idade:.1f} anos.")
print(f"Media de idade masculina é: {idade_media_masculina:.1f} anos.")
print(f"Media de idade feminina é: {idade_media_feminina:.1f} anos.")

print(f"\nMédia salarial geral é: R${media_salarial:.2f}")
print(f"Média salarial masculina é: R${media_salarial_masculina:.2f}")
print(f"Média salarial feminina é: R${media_salarial_feminina:.2f}")