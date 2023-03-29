temperatura = str(input('Digite a temperatura Cº: '))

try:
    if temperatura.count(',') == -1:
        farenhait = float((temperatura * 9/5) + 32)
        print(f'\033[32mSe a temperatura for {temperatura:.2f}Cº, então em farenheit será {farenhait:.2f}F!\033[m')

    else:
        temperatura = float(temperatura.replace(",", "."))
        farenhait = float((temperatura * 9/5) + 32)
        print(f'\033[32mSe a temperatura for {temperatura:.2f}Cº, então em farenheit será {farenhait:.2f}F!\033[m')

except:
    print('\033[31mPor favor,digite apenas números.\033[m')
