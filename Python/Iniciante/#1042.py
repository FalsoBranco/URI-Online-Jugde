entrada = input().split()

arr = [int(valor) for valor in entrada]

for valor in sorted(arr):
    print(valor)
print()
for valor in arr:
    print(valor)
