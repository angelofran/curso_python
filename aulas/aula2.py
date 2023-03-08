# Tipos principais
inteiro = 10
floatuat = 10.0
boolean = True
string = "Angelo"

# Tipos especiais
tupla = tuple()
lista = list()
dicti = dict()


#print("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(type(inteiro), type(floatuat), type(bool), type(str), type(lista), type(tupla), type(dicti)))

# n = bool(input("Digite um valor: "))
# if n == False:
#   print("Digite um número ou palavra")
# else:
#    print(f"O resultado foi bom")


m = input("Digite um valor: ")
if m.isnumeric():
    print(m)    

elif m.isalpha():
    print(m)
    
else:
    print("Não quero printar")