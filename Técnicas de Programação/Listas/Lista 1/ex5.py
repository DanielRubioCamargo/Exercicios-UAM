dadosFrutas = dict()
listaFrutas = list()
resp = ""
while resp != "N":
    fruta = str(input("Insira uma fruta : ")).strip()
    precoFruta = float(input("Insira o seu respectivo preço : "))
    dadosFrutas = {"fruta":fruta,"preco":precoFruta}
    listaFrutas.append(dadosFrutas.copy())
    dadosFrutas.clear()
    resp = str(input("Quer continuar? [S/N] : ")).strip().upper()
for i in listaFrutas:
    print("Nome da fruta : {} - Preço da fruta : R${:.2f}".format(i["fruta"],i["preco"]))
