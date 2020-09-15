valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
print(valor)
for i in range(len(notas)):
    contador = 0
    while valor >= notas[i]:
        contador += 1
        valor -= notas[i]
    print("{} nota(s) de R$ {},00".format(contador, notas[i]))
