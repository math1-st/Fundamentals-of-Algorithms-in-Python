print("Cálculo de aluguel de carro.\n")

kilometragem = float(input("Digite a kilometragem do carro: "))
diarias = float(input("Digite por quantos dias o carro foi alugado: "))

calculo = (kilometragem * 0.15) + (diarias * 60)

print(f"O seu total é: R${calculo:.2f}.")