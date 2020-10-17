entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])


maior = (a + b + abs(a - b)) / 2
if maior > c:
    print("{:.0f} eh o maior".format(maior))
else:
    print("{:.0f} eh o maior".format(c))
