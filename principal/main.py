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
jogo_dica = input(str("(0)Jogar \n(1)Solicitar dica\n(2)Sair do jogo\n"))

chances = 5
dicas_solicitadas = 0

while chances > 0:
    if jogo_dica == "0":
        input(str("Informe uma letra: "))
        chances = chances - 1#faz 5 vezes estando certo ou errado
    elif jogo_dica =="1":#resolver como mostrar uma dica por vez
        print(dicas)
        dicas_solicitadas = dicas_solicitadas + 1
    elif jogo_dica =="2":
        break
