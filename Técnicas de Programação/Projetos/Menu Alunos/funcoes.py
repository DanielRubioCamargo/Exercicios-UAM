# Modulo para as funções

def criar_cabecalho(titulo:str,tamanhoLinha = 55):
    print("-"*tamanhoLinha)
    print(titulo.center(tamanhoLinha))
    print("-"*tamanhoLinha)


def criar_menu(lista,titulo:str,tamanhoLinha = 55):
    print("-"*tamanhoLinha)
    print(titulo.center(tamanhoLinha))
    print("-"*tamanhoLinha)
    for i,c in enumerate(lista):
        print("{} --> {}".format(i+1,c))
    print("-"*tamanhoLinha)


def cadastrar_usuario(lista,nome:str,email:str):
    dadosAlunos = {"nome":nome,"email":email}
    lista.append(dadosAlunos.copy())
    dadosAlunos.clear()


def exibir_usuarios_cadastrados(lista):
    for i,c in enumerate(lista):
        print("{} --> {}".format(i+1,c["nome"].title()))


def exibir_usuarios_cadastrados_ordem_alfabetica(lista):
    listaAux = list()
    for i in lista:
        listaAux.append(i["nome"].title())
    listaAux.sort()
    for i,c in enumerate(listaAux):
        print("{} --> {}".format(i+1,c))


def verificar_usuario(lista,nome:str):
    for i,c in enumerate(lista):
        if c["nome"] == nome:
            print("Há um aluno com esse nome!")
            break
        elif i == len(lista) - 1:
            print("Não encontramos nenhum aluno com esse nome!")


def remover_aluno(lista,email:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            lista.pop(i)


def alterar_nome_usuario(lista,email:str,novoNome:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            c["nome"] = novoNome
