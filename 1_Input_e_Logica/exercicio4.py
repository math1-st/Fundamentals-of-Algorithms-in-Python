# # Faça um programa que pergunte quanto a pessoa ganha por hora e
# o número de horas trabalhas no mês. Calcule e mostre o total
# do salário no referido mês, sabendo-se que são descontados 11%
# para o imposto de renda, 8% para o INSS e 5% para o sindicato.

print("Cálculo de salário líquido.\n")

ganho_hora = float(input("Quanto você ganha por hora: "))
horas_mes = float(input("Quantas horas você trabalha no mês: "))

salario_bruto = ganho_hora * horas_mes
desconto_imposto = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

print(f"\nSeu salário bruto é: R${salario_bruto}\n")

salario_liquido = (salario_bruto - desconto_imposto - desconto_inss - desconto_sindicato)

print("Salário será descontado do: ")
print(f"- Imposto de Renda (11%): R${desconto_imposto}")
print(f"- INSS (8%): R${desconto_inss}")
print(f"- Sindicato (5%:) R${desconto_sindicato}\n")

print(f"Seu salário líquido é: R${salario_liquido}")