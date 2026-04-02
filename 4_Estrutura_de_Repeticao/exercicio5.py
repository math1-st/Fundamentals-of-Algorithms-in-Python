while True:
    
    a = int(input("Digite um número entre 1 e 10: "))

    if a <= 0 or a >= 10:
        print("Digite um número válido.")
    else:
        print("Válido")
        break