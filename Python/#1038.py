
entrada = input().split()
codigo = int(entrada[0])
quantidade = int(entrada[1])


if codigo == 1:
    print('Total: R$ {:.2f}'.format(4.00 * quantidade))
elif codigo == 2:
    print('Total: R$ {:.2f}'.format(4.50 * quantidade))
elif codigo == 3:
    print('Total: R$ {:.2f}'.format(5.00 * quantidade))
elif codigo == 4:
    print('Total: R$ {:.2f}'.format(2.00 * quantidade))
else:
    print('Total: R$ {:.2f}'.format(1.50 * quantidade))
