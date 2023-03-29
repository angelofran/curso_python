from random import shuffle

lista = []

for i in range(4):
    n = str(input(f'Digite o {i+1}ª nome: '))
    lista.append(n)

shuffle(lista)

print('A ordem de apresentação do trabalho será')
for i in lista:
    print(f'{i}', end=', ')

print('Fim.')