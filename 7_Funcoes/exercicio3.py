from random import randint

def somarFaces():

    return randint(1, 6) + randint(1, 6)

lista_soma_faces = []

for _ in range(1000):

    lista_soma_faces.append(somarFaces())

dicionario = {}

for numero in lista_soma_faces:

    if numero in dicionario:
        dicionario[numero] += 1
    else:
        dicionario[numero] = 1
        
for chave, valor in dicionario.items():
    print(f"{chave}: {valor/1000:.2%}")