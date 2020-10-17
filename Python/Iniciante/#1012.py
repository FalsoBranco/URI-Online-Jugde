entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
PI = 3.14159
tri = (A * C) / 2
cir = PI * C ** 2
tra = ((A + B) * C) / 2
qua = B ** 2
ret = A * B


print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(cir))
print("TRAPEZIO: {:.3f}".format(tra))
print("QUADRADO: {:.3f}".format(qua))
print("RETANGULO: {:.3f}".format(ret))
