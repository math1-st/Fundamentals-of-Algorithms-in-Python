x = 0
aprovados = 0
soma = 0

qnt_alunos = 80
while x < qnt_alunos:

    x = x + 1
    a = int(input(f"Digite a nota do aluno nº{x}: "))

    soma = soma + a

    if a >= 6:
        aprovados = aprovados + 1

media = soma / qnt_alunos

print(f"Média é: {media}")
print(f"Quantidade de alunos aprovados é: {aprovados}")
