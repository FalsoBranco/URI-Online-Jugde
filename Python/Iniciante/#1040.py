notas = input().split()
peso = [2, 3, 4, 1]
media = round(sum([float(nota) * peso for nota, peso in zip(notas, peso)]) / sum(peso), 1)

print("Media:", media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input(""))
    print("Nota do exame:", nota_exame)
    media = (media + nota_exame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", media)
