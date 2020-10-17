entrada = input().split()
a, b, c, d = [int(x) for x in entrada]

aceito = False


if b > c and d > a:
    if (c + d) > (a + b):
        if c > 0 and d > 0:
            if a % 2 == 0:
                aceito = True

if aceito:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
