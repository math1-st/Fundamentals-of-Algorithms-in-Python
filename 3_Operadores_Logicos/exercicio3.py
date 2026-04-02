altura = float(input("Digite a altura do indivíduo em metros: "))
genero = input("Você é homem ou mulher: ")

if genero == "homem":
    peso = (72.7 * altura) - 58
elif genero == "mulher":
    peso = (62.1 * altura) - 44.7

print(f"Peso ideal: {peso}kg")
