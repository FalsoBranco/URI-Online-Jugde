entrada1 = input().split()
entrada2 = input().split()


total = (float(entrada1[1]) * float(entrada1[2])) + (float(entrada2[1]) * float(entrada2[2]))


print("VALOR A PAGAR: R$ {:.2f}".format(total))
