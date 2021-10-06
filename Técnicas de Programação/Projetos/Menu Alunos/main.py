# Programa principal
from funcoes import *
from time import sleep

def main():
    listaAlunos = list()
    listaOpcoes = ["Cadastrar novo usuário.","Exibir usuários cadastrados.","Exibir usuários cadastrados por ordem alfabética.","Verificar se existe um usuário na lista.","Remover um usuário da lista.","Alterar nome de um usuário."]
    criar_cabecalho("Seja bem vindo(a)!",True)
    while True:
        criar_menu(listaOpcoes,"Opções")
        try:
            opcao = int(input("Insira sua opção : "))
        except:
            print("Erro de tipo ou valor do dado inserido!")
        else:
            if opcao == 1:
                nome = str(input("Insira seu nome completo : ")).strip().title()
                email = str(input("Insira seu endereço de email : ")).strip()
                cadastrar_usuario(listaAlunos,nome,email)
            elif opcao == 2:
                criar_cabecalho("Lista de alunos por ordem de cadastro")
                exibir_usuarios_cadastrados(listaAlunos)
                sleep(1.5)
            elif opcao == 3:
                criar_cabecalho("Lista de alunos em ordem alfabetica")
                exibir_usuarios_cadastrados_ordem_alfabetica(listaAlunos)
                sleep(1.5)
            elif opcao == 4:
                nomeUsuario = str(input("Insira o nome do usuário desejado : ")).strip().title()
                temAluno = verificar_usuario_nome(listaAlunos,nomeUsuario)
                if temAluno == True:
                    print("Há um usuário com esse nome presente na lista!")
                else:
                    print("Não foi encontrado nenhum usuário com esse nome na lista!")
                sleep(1.5)
            elif opcao == 5:
                emailUsuario = str(input("Insira o email do usuário que se deseja excluir da lista : ")).strip()
                temAluno2 = verificar_usuario_email(listaAlunos,emailUsuario2)
                if temAluno2 == True:
                    remover_aluno(listaAlunos,emailUsuario)
                else:
                    print("Não foi possível executar a remoção, endereço de email não existe na lista!")
            elif opcao == 6:
                emailUsuario2 = str(input("Insira o email do usuário que se deseja alterar o nome na lista : ")).strip()
                temAluno3 = verificar_usuario_email(listaAlunos,emailUsuario2)
                if temAluno3 == True:
                    novoNome = str(input("Insira o novo nome do usuário cujo o email é {} : ".format(emailUsuario2)))
                    alterar_nome_usuario(listaAlunos,emailUsuario2,novoNome)
                else:
                    print("Não foi possível executar a alteração, endereço de email não existe na lista!")
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()