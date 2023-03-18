# Antecessor e sucessor
import tqdm
import time

num = input('Escreva um número: ')

if num.isnumeric():
    print('ANALIZANDO PROFUNDAMENTE...')
    for i in tqdm.tqdm(range(10)):
        time.sleep(2)
    print(f'O sucessor será {int(num) + 1}')
    print(f'O antecessor será {int(num) - 1}')

else:
    print('ANALIZANDO PROFUNDAMENTE...')
    for i in tqdm.tqdm(range(10)):
        time.sleep(2)

    print('\033[31mPor favor, digite apenas números\033[m')