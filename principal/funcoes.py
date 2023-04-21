import os

def limpar_tela():
    os.system("cls")

def tela_inicial():
    print("*-"*10)
    print("JOGO DA FORCA")
    print("*-"*10)
    input("Press enter to continue...")

def criar_base_dados():
    try:
        arquivo = open("banco_dados.txt","r")
        arquivo.close()
    except:
        arquivo = open("banco_dados.txt","w")
        print("Base de dados criada com sucesso")
        input("Press enter to continue...")
        arquivo.close()

def menu():
    # exibe as opções do menu e retorna a opção selecionada pelo usuário
    opcoes = ["(0)Solicitar dica\n(1)Jogar\n(2)Sair"]
    print("Menu:")
    print("\n".join(opcoes))
    opcao = input("Escolha uma opção: ")
    return opcao

