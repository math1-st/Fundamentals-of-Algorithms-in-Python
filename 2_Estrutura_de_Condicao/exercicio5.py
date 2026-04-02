ano_atual = int(input("Em que ano estamos: "))
ano_usuario = int(input("Em que ano você nasceu: "))

if ano_atual - ano_usuario >= 18:
    print("Você pode tirar a CNH.")
else:
    print("Você não pode tirar a CNH.")