entrada = input("").split()


a, b, c = [float(x) for x in entrada]


delta = b * b - (4 * a * c)
if delta > 0 and a != 0:
    R1 = (-b + delta ** (1.0 / 2)) / (2 * a)
    R2 = (-b - delta ** (1.0 / 2)) / (2 * a)

    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))
else:
    print("Impossivel calcular")
