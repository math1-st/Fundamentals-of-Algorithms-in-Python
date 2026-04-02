temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]

soma_media = 0
maior_temp = 0
menor_temp = 0
for media in temperaturas:

    soma_media += media

    if maior_temp < media:
        maior_temp = media

    if menor_temp > media:
        menor_temp = media 

media_final = soma_media / len(temperaturas)

print(media_final)
print(maior_temp)
print(menor_temp)