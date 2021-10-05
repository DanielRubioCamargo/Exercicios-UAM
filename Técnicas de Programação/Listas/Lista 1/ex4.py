def mostrar_cidades_7letras(listaCidades : str):
    num = int(input("Quantas cidades deseja-se inserir? : "))
    for i in range(num):
        listaCidades.append(str(input("Insira o nome da cidade : ")))
    print("O usário escolheu {} cidades!".format(num))
    print("Lista das cidades com mais de 7 letras : ")
    for i in listaCidades:
        if len(i) >= 7:
            print("-> {}".format(i))

def main():
    cidades = list()
    mostrar_cidades_7letras(cidades)

if __name__ == "__main__":
    main()