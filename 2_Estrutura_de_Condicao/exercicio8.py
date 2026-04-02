from math import ceil

pi = 3.1415

altura_cilindro = float(input("Qual a altura do cilindro: "))
raio_cilindro = float(input("Qual o raio do cilindro: "))

perimetro_cilindro = 2 * pi * raio_cilindro
area_lateral_cilindro = altura_cilindro * perimetro_cilindro

area_bases_cilindro = 2 * pi * (raio_cilindro ** 2) # SÃO DUAS BASES.

area_total = area_lateral_cilindro + (area_bases_cilindro) 

qnt_litros_cilindro = area_total / 3

print(f"Área a ser pintada: {area_total:.2f}")
print(f"Quantidade de litros necessários: {qnt_litros_cilindro:.2f}")

qnt_latas = ceil(qnt_litros_cilindro / 5)
print(f"Quantidade de latas: {qnt_latas}")

valor_lata_und = 50

if qnt_latas == 1:
    valor_lata_und = 50
    print(f"Preço unitário da lata R${valor_lata_und}")
elif qnt_latas == 2:
    valor_lata_und = 48
    print(f"Preço unitário da lata R${valor_lata_und}")
elif qnt_latas == 3:
    valor_lata_und = 46
    print(f"Preço unitário da lata R${valor_lata_und}")
else:
    valor_lata_und = 45
    print(f"Preço unitário da lata R${valor_lata_und}")

custo = qnt_latas * valor_lata_und
print(f"Custo total: {custo}")