N = int(input())

horas = N//3600
minutos = N // 60 % 60
segundos = N % 60
print("{:.0f}:{:.0f}:{:.0f}".format(horas, minutos, segundos))
