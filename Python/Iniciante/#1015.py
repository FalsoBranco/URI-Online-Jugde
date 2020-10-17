entrada1 = input().split()
entrada2 = input().split()


x1, y1 = float(entrada1[0]), float(entrada1[1])
x2, y2 = float(entrada2[0]), float(entrada2[1])
srq = (((x2 - x1)**2) + ((y2 - y1)**2)) ** (1/2)
print("{:.4f}".format(srq))
