cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))

hip = ((cat1 ** 2) + (cat2 ** 2)) ** (1/2)
print(f'Para os dados acima a hipotenusa é {hip:.2f}')

