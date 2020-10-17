"""entrada = float(input(""))


notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    res = int(entrada / nota)
    print("{:.0f} nota(s) de R$ {}.00".format(res, nota))

    entrada -= round(res * nota, 2)


print("MOEDAS:")
for moeda in moedas:
    res = int(round(entrada, 2) / moeda)
    print("{:.0f} moeda(s) de R$ {:.2f}".format(res, moeda))
    entrada = entrada - res * moeda"""

entrada = float(input(""))


notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    res = entrada // nota
    print("{:.0f} nota(s) de R$ {}.00".format(res, nota))

    entrada -= round(res * nota, 2)


print("MOEDAS:")
for moeda in moedas:
    res = round(entrada, 2) // moeda
    print("{:.0f} moeda(s) de R$ {:.2f}".format(res, moeda))
    entrada = entrada - res * moeda
