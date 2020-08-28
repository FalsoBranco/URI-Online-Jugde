while True:
    lst = []
    X = int(input())

    if X % 2 == 0:
        lst.append(X)
    else:
        lst.append(X + 1)

    if X == 0:
        break

    while len(lst) != 5:
        lst.append(lst[-1]+2)
    print(sum(lst))
