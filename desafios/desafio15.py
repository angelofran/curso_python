dias = int(input("Por quantos dias o carro foi alugado? "))
distancia = float(input("Qunatos km foram percorrido? "))

resultado = (dias * 60) + (distancia * 0.15)

print(f'O preço a pagar é de {resultado}R$')