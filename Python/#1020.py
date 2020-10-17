
dias = int(input())
ano = dias // 365
mes = dias % 365 // 30
dia = dias % 365 % 30

print("{:.0f} ano(s)\n{:.0f} mes(es)\n{:.0f} dia(s)".format(ano, mes, dia))
