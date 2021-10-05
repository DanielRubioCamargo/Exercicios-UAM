cidades = list()
num = int(input("Quantas cidades deseja-se inserir? : "))
for i in range(num):
    cidades.append(str(input("Insira o nome da cidade : ")))
print("O usário escolheu {} cidades!".format(num))
print("Lista das cidades : ")
for i in cidades:
    print("-> {}".format(i))