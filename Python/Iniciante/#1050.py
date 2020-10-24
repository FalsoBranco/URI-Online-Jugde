DISTRICT = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte", ]

DDD = [61, 71, 11, 21, 32, 19, 27, 31]


valor = int(input())

if valor in DDD:
    index = DDD.index(valor)
    print(DISTRICT[index])
else:
    print("DDD nao cadastrado")
