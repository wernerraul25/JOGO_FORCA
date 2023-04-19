from funcoes import limpar_tela

limpar_tela()

print("-="*20)
print("JOGO DA FORCA")
print("-="*20)
input("Press enter to continue...")

limpar_tela()

nome_desafiante = input("Nome do desafiante: ")
nome_competidor = input("Nome do competidor: ")

limpar_tela()

palavra_chave = input("Digite a palavra chave: ")
dicas = [input("Dica 1: "), input("Dica 2: "), input("Dica 3: ")]


limpar_tela()

print("A palavra chave contém", len(palavra_chave), "letra(s)!")
input("press enter to continue...")
limpar_tela()

print("Selecione a opção que deseja digitando o número equivalente!")
jogo_dica = input(str("(0)Jogar \n(1)Solicitar dica\n"))

if jogo_dica == "0":
    input(str("Informe uma letra: "))
elif jogo_dica =="1":
    for dica in dicas:
        print(dica)


dicas_solicitadas = 0
chances = 5
