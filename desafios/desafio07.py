soma = 0
for i in range(2):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    soma += nota

média = soma / (i + 1)
print(f'A média aritimética é {média:.2f}')