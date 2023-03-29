valor = str(input('Digite o valor em R$: '))

if valor.count(',') == -1:
    print(f'Com {valor}R$ você pode comprar {float(valor) / 3:.2f}US$.')

else:
    valor = float(valor.replace(",", "."))
    print(f'Com {valor}R$ você pode comprar {valor / 3:.2f}US$.')