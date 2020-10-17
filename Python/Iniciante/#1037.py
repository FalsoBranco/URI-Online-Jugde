valor = float(input(""))

intervalos = ("[0, 25]", "(25, 50]", "(50, 75]", "(75, 100]")
intervalox = ([0, 25], [25.1, 50.0], [50, 75], [75, 100])

for i, x in enumerate(intervalox):
    if valor in range(x[0], x[1]):
        print(intervalos[i])
