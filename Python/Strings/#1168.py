casos = int(input())


leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
for caso in range(casos):
    total = 0
    valor = input()
    for i in valor:
        if i != "0":
            total += leds[int(i) - 1]
            continue
        total += leds[-1]
    print(total, "leds")
