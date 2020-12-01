
casos = int(input())

for caso in range(casos):
    testes = int(input())
    soma = 0
    for teste in range(testes):
        letras = input().lower()
        for posicao, letra in enumerate(letras):
            valor = (ord(letra)-97) + teste + posicao

            soma += valor
    print(soma)
