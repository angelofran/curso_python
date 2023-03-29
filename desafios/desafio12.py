valor_produto = str(input('Digite o valor do produto, Kz '))

try:
    if valor_produto.count(',') == -1:
        desconto = valor_produto - (valor_produto * (5/100))
        print(f'\033[32mSe o preço do produto for {valor_produto:.2f}Kz, então quando aplicado um desconto de 5% você ficará com {desconto:.2f}Kz\033[m')

    else:
        valor_produto = float(valor_produto.replace(",", "."))
        desconto = valor_produto - (valor_produto * (5/100))
        print(f'\033[32mSe o preço do produto for {valor_produto:.2f}Kz, então quando aplicado um desconto de 5% você ficará com {desconto:.2f}Kz\033[m')

except:
    print('\033[31mPor favor,digite apenas números.\033[m')
