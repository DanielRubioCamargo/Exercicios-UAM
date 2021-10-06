# Modulo para as funções

def criar_cabecalho(titulo:str,hasEqual = False,tamanhoLinha = 55):
    if hasEqual == True:
        print("-=-"*18)
        print(titulo.center(tamanhoLinha))
        print("-=-"*18)
    else:
        print("-"*tamanhoLinha)
        print(titulo.center(tamanhoLinha))
        print("-"*tamanhoLinha)


def criar_menu(lista,titulo:str,tamanhoLinha = 55):
    print("-"*tamanhoLinha)
    print(titulo.center(tamanhoLinha))
    print("-"*tamanhoLinha)
    for i,c in enumerate(lista):
        print("[{}] {}".format(i+1,c))
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


def verificar_usuario_nome(lista,nome:str):
    for i,c in enumerate(lista):
        if c["nome"] == nome:
            return True
            break
        elif i == len(lista) - 1:
            return False


def verificar_usuario_email(lista,email:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            return True
            break
        elif i == len(lista) - 1:
            return False


def remover_aluno(lista,email:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            lista.pop(i)
            print("Aluno {} removido da lista com sucesso!".format(c["nome"]))


def alterar_nome_usuario(lista,email:str,novoNome:str):
    cont = 0
    for i,c in enumerate(lista):
        if c["email"] == email:
            print("Alteração de {} para {} foi um sucesso!".format(c["nome"],novoNome))
            c["nome"] = novoNome
            break
