from random import randint

lista = []

for i in range(4):
    n = str(input(f'Digite o {i+1}ª nome: '))
    lista.append(n)


print(f'O nome sorteado foi {lista[randint(0, 3)]}')
