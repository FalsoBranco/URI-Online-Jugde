
X = int(input())
Y = int(input())

if X > Y:
    n1 = Y
    n2 = X
else:
    n1 = X
    n2 = Y

soma = 0
for i in range(n1, n2+1):
    if i % 13 != 0:
        soma += i


print(soma)
