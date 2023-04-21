from funcoes import limpar_tela, tela_inicial

limpar_tela()

tela_inicial()

limpar_tela()

nome_desafiante = input("Nome do desafiante: ")
nome_competidor = input("Nome do competidor: ")

limpar_tela()

palavra_chave = input("Digite a palavra chave: ")
dica1 = input("Dica 1: ")
dica2 = input("Dica 2: ")
dica3 = input("Dica 3: ")

letras_descobertas = []

limpar_tela()

tamanho_palavra_chave = len(palavra_chave)
palavra_oculta = '*' * tamanho_palavra_chave
dicas_solicitadas = 0

print("A palavra chave contém", tamanho_palavra_chave, "letra(s)!")
input("press enter to continue...")

limpar_tela()

print("Selecione a opção que deseja digitando o número equivalente!")
opcao = input("(0)Solicitar dica \n(1)Jogar\n(2)Sair do jogo\n")

aleatorio = 0
try:
    while aleatorio < 2:
        aleatorio += 1
        if opcao =="0":
            dicas_solicitadas += 1
            if dicas_solicitadas > 3:
                print("Você solicitou o número máximo de dicas!")
            else:
                if dicas_solicitadas == 1:
                    print("Dica 1:", dica1)
                    continue
                elif dicas_solicitadas == 2:
                    print("Dica 2:", dica2)
                    continue
                else:
                    print("Dica 3:", dica3)
                #bug, fecha o jogo ao pedir dica
        elif opcao == "1":
            letra = input("Digite uma letra: ")
            
        
        #elif opcao =="2":
        #falta opção 2
        else:
            print("Opção inválida!")
            continue   
except:
    print("O jogo acabou!")