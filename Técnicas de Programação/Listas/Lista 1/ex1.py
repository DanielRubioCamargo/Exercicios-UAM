lista = list()
for i in range(5):
    lista.append(int(input("Insira um valor : ")))
lista.sort()
print(lista)
lista.pop(3)
print(lista)