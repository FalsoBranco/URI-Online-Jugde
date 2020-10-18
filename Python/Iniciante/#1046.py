valores = input().split()

inicio = int(valores[0])
final = int(valores[1])

if inicio == final or inicio == 0 == final:
    print("O JOGO DUROU 24 HORA(S)")
elif inicio < final:
    print("O JOGO DUROU {} HORA(S)".format(final - inicio))
elif inicio > final:
    print("O JOGO DUROU {} HORA(S)".format((24 - inicio) + final))
else:
    print()
