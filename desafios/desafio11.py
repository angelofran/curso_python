largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

área = largura * altura
tinta_necessaria = área / 2

print(f'A sua parede possui uma dimensão de {largura:.2f}x{altura:.2f}, e a sua área é de {área:.2f}m^2')
print(f'Para pintá-la precisará de {tinta_necessaria:.1f}l.')