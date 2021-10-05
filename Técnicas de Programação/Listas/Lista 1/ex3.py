def mostrar_cidades(listaCidades : str):
    num = int(input("Quantas cidades deseja-se inserir? : "))
    for i in range(num):
        listaCidades.append(str(input("Insira o nome da cidade : ")))
    print("O usário escolheu {} cidades!".format(num))
    print("Lista das cidades : ")
    for i in listaCidades:
        print("-> {}".format(i))
    
def main():
    cidades = list()
    mostrar_cidades(cidades)

if __name__ == "__main__":
    main()