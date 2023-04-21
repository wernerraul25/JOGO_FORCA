from funcoes import limpar_tela, tela_inicial, menu

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

try:
    while True:
        opcao = menu()
        if opcao =="0":
            dicas_solicitadas += 1
            if dicas_solicitadas > 3:
                print("Você solicitou o número máximo de dicas!")
            else:
                if dicas_solicitadas == 1:
                    print("Dica 1:", dica1)
                elif dicas_solicitadas == 2:
                    print("Dica 2:", dica2)
                else:
                    print("Dica 3:", dica3)
                #bug, fecha o jogo ao pedir dica
            pass
        elif opcao == "1":
            for i in range(0, len(palavra_chave)):
                letras_descobertas.append("*")

            acertou = False

            while acertou == False :
                letra = str(input("DIgite a letra: "))

                for i in range(0, len(palavra_chave)):
                    if letra == palavra_chave[i]:
                        letras_descobertas[i] = letra

                    print(letras_descobertas[i])

                acertou = True

                for x in range(0, len(letras_descobertas)):
                    if letras_descobertas[x] == "*":
                        acertou = False
            break
        elif opcao =="2":
            break
        else:
            print("Opção inválida, tente novamente!")
except:
    print("O jogo acabou!")
