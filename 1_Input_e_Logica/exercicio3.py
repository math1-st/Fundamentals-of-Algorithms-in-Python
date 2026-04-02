print("Cálculo da soma de dias, horas, minutos e segundos em apenas segundos.")

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

calculo = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos

print(f"Resultado: {calculo:,d} segundos")

# Adicionar :,d ao final de calculo para facilitar a leitura do número.