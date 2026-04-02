def procuraChave(dicionario, valorProcurado):

    lista = []

    for key, value in dicionario.items():

        if value == valorProcurado:

            lista.append(key)

    return lista

a = {
    'um': 1,
    'dois': 2,
    'tres': 3,
    'exemplo': 1
}

print(procuraChave(a, 3))