from funcoes import limpar_tela

limpar_tela()

print("*-"*10)
print("JOGO DA FORCA")
print("*-"*10)
input("Press enter to continue...")

limpar_tela()

nome_desafiante = input("Nome do desafiante: ")
nome_competidor = input("Nome do competidor: ")

limpar_tela()

palavra_chave = input("Digite a palavra chave: ")
letras_descobertas = []
dicas = [input("Dica 1: "), input("Dica 2: "), input("Dica 3: ")]


limpar_tela()

print("A palavra chave contém", len(palavra_chave), "letra(s)!")
input("press enter to continue...")
limpar_tela()

print("Selecione a opção que deseja digitando o número equivalente!")
opcoes_de_jogo = input(str("(0)Jogar \n(1)Solicitar dica\n(2)Sair do jogo\n"))

chances = 5
dicas_solicitadas = 0

try:
    while chances > 0:
        if opcoes_de_jogo == "0":
            for i in range(0, len(palavra_chave)):
                letras_descobertas.append("*")

            acertou = False

            while acertou == False :
                letra = str(input("Digite a letra: "))

                for i in range(0, len(palavra_chave)):
                    if letra == palavra_chave[i]:
                        letras_descobertas[i] = letra

                    print(letras_descobertas[i])

                acertou == True

                for x in range(0, len(letras_descobertas)):
                    if letras_descobertas[x] == "*":
                        acertou = False
#bug, não termina nunca                
        elif opcoes_de_jogo =="1":#resolver como mostrar uma dica por vez
            print(dicas)
            dicas_solicitadas = dicas_solicitadas + 1
        elif opcoes_de_jogo =="2":
            break
except:
    print("O jogo acabou!")