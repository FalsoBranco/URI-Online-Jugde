valores = input().split()


a, b, c = [float(valor) for valor in valores]
isPossible = False
if a + b > c and b + c > a and c + a > b:
    isPossible = True

if isPossible:
    print("Perimetro =", a + b + c)
else:
    print("Area =", ((a + b) * c) / 2)
