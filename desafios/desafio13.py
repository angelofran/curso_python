salario = str(input('Digite o valor do produto, Kz '))

try:
    if salario.count(',') == -1:
        aumento = float(salario) + (float(salario) * (15/100))
        print(f'\033[32mSe o funcionário ganha {salario:.2f}Kz, então quando aplicado um aumento de 15% ele ficará com {aumento:.2f}Kz\033[m')

    else:
        salario = float(salario.replace(",", "."))
        aumento = float(salario) + (float(salario) * (15/100))
        print(f'\033[32mSe o funcionário ganha {salario:.2f}Kz, então quando aplicado um aumento de 15% você ficará com {aumento:.2f}Kz\033[m')

except:
    print('\033[31mPor favor,digite apenas números.\033[m')
    