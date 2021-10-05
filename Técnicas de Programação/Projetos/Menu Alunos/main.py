# Programa principal
from funcoes import *
from time import sleep

def main():
    listaAlunos = list()
    listaOpcoes = ["Cadastrar novo usuário","Exibir usuários cadastrados","Exibir usuários cadastrados por ordem alfabetica","Verificar se existe um usuário na lista","Remover um usuário da lista","Alterar nome de um usuário"]
    criar_cabecalho("Seja bem vindo(a)!")
    while True:
        criar_menu(listaOpcoes,"Opções")
        opcao = int(input("Insira sua opção : "))
        if opcao == 1:
            nome = str(input("Insira seu nome completo : ")).strip().title()
            email = str(input("Insira seu endereço de email : ")).strip()
            cadastrar_usuario(listaAlunos,nome,email)
        elif opcao == 2:
            criar_cabecalho("Lista de alunos por ordem de cadastro")
            exibir_usuarios_cadastrados(listaAlunos)
            sleep(1)
        elif opcao == 3:
            criar_cabecalho("Lista de alunos em ordem alfabetica")
            exibir_usuarios_cadastrados_ordem_alfabetica(listaAlunos)
            sleep(1)
        elif opcao == 4:
            nomeUsuario = str(input("Insira o nome do usuário desejado : ")).strip().title()
            verificar_usuario(listaAlunos,nomeUsuario)
        elif opcao == 5:
            emailUsuario = str(input("Insira o email do usuário que se deseja excluir da lista : ")).strip()
            remover_aluno(listaAlunos,emailUsuario)
        elif opcao == 6:
            emailUsuario2 = str(input("Insira o email do usuário que se deseja alterar o nome na lista : ")).strip()
            novoNome = str(input("Insira o novo nome do usuário cujo o email é : {}".format(emailUsuario2)))
            alterar_nome_usuario(listaAlunos,emailUsuario2,novoNome)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()