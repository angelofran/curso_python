from math import sin, cos, tan, radians

an = radians(float(input('Digite o ângulo(º): '))) # Lendo o Ângulo, e convertendo para radiano

seno = sin(an)
coss = cos(an)
tang = tan(an)

print(f'Para os dados fornecidos o seno será {seno:.2f}, o cosseno {coss:.2f} e a tangente {tang:.2f}.')
