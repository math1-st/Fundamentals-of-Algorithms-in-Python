salario = float(input("Digite seu salário: "))

if salario > 1250:
    novo_salario = salario * 1.1
    print(f"{novo_salario:1f}")
else:
    novo_salario = salario * 1.15
    print(f"{novo_salario:1f}")