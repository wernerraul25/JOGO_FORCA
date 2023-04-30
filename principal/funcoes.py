import os

def limpar_tela():
    os.system("cls")

def tela_inicial():
    print("*-"*10)
    print("JOGO DA FORCA")
    print("*-"*10)
    input("Press ENTER to continue...")

def criar_historico():
    try:
        arquivo = open("historico.txt","r")
        arquivo.close()
    except:
        arquivo = open("historico.txt","w")
        print("Base de dados criada com sucesso")
        input("Press enter to continue...")
        arquivo.close()

def menu():
    # exibe as opções do menu e retorna a opção selecionada pelo usuário
    opcoes = ["(1)Jogar\n(2)Solicitar dica\n(3)Ver resultados anteriores"]
    print("Menu:")
    print("\n".join(opcoes))
    opcao = input("Escolha uma opção: ")
    return opcao

def historico(nome_desafiante, nome_competidor, palavra_chave, vencedor):
    arquivo = open("historico.txt","a")
    if vencedor == nome_competidor:
        arquivo.write("Vencedor: Competidor " + nome_competidor + ", Perdedor: Desafiante " + nome_desafiante + ", Palavra-chave: " + palavra_chave)
        arquivo.write("\n")
    else:
        arquivo.write("Vencedor: Desafiante " + nome_desafiante + ", Perdedor: Competidor " + nome_competidor+ ", Palavra-chave: " + palavra_chave)
        arquivo.write("\n")
    arquivo.close()

def ler_historico():
    arquivo = open("historico.txt","r")
    dados = arquivo.read()
    arquivo.close()
    print(dados)

def convert_caps(texto):
    return texto.upper()

def teste_vazio(texto):
    while not texto:
        texto = input("Nome inválido! Digite novamente: ")
        return texto
    '''while True:
        if texto.strip():
            return texto
        else:
            print("Você não digitou nada, tente novamente!")'''
    '''while True:
        if texto:
            return texto
            break
        else:
            print("Você não digitou nada, tente novamente!")'''

def menu_final():
    opcao2 = input("\nMenu:\n(1)Jogar Novamente\n(2)Sair\n(3)Ver histórico de partidas\nEscolha uma opção: ")
    return opcao2