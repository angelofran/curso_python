nome = str(input('SEU NOME COMPLETO: ')).strip()

print(f'Com letras MAIÚSCULAS: {nome.upper()}')
print(f'Com letras MINÚSCULAS: {nome.lower()}')
print(f'Tamanho (sem considerar espaços): {len(nome.replace(" ", ""))}')
print(f'O primeiro nome tem: {len(nome.split()[0])}')
