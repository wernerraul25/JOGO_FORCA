from funcoes import limpar_tela, tela_inicial, menu, historico, ler_historico, convert_caps, menu_final

try:
    while True:
        limpar_tela()

        tela_inicial()

        limpar_tela()

        nome_competidor = input("Nome do competidor: ")
        nome_desafiante = input("Nome do desafiante: ")

        limpar_tela()

        palavra_chave = input("Digite a palavra chave: ")
        dica1 = input("Dica 1: ")
        dica2 = input("Dica 2: ")
        dica3 = input("Dica 3: ")

        limpar_tela()

        tamanho_palavra_chave = len(palavra_chave)
        palavra_oculta = '*' * tamanho_palavra_chave
        
        print("A palavra chave contém", tamanho_palavra_chave, "letra(s)!")
        input("Press ENTER to continue...")

        dicas_solicitadas = 0
        erros = 0
        tentativas = []
        acertos= []
        vencedor = []
        dica = 0

        limpar_tela()

        while True:
            opcao = menu()
            if opcao =="2":
                if dica==0:
                    print("Dica 1: ", dica1)
                    dica = dica+1
                    input("Press ENTER to continue...")
                    limpar_tela()

                elif dica==1:
                    print("Jogue para desbloquear mais dicas!")
                    input("Press ENTER to continue...")
                    dica = dica + 1
                    limpar_tela()

                elif dica==2:
                    print("Dica 1: ", dica1,"\n""Dica 2: ", dica2)
                    dica = dica+1
                    input("Press ENTER to continue...")
                    limpar_tela()
                else:
                    print("Dica 1:", dica1,"\nDica 2:", dica2, "\nDica 3:",dica3,"\nEssas são as dicas!")
            elif opcao == "1":
                letra = input("Digite uma letra: ")
                if letra in tentativas:
                    print("Você já tentou essa letra anteriormente.")
                elif letra not in palavra_chave:
                    print("Essa letra não pertence a palavra.")
                    tentativas.append(letra)
                    erros += 1
                    print("Total de erros:", erros)
                    input("Press ENTER to continue...")
                    limpar_tela()
                else:
                    print("Você acertou a letra:")
                    acertos.append(letra)
                    palavra = ""
                    for letra in palavra_chave:
                        if letra in acertos:
                            palavra += letra
                        else:
                            palavra += "*"
                    print(palavra)
                    if palavra == palavra_chave:
                        limpar_tela()
                        win_upper = convert_caps(nome_competidor)
                        print(win_upper,"parabéns, você acertou a palavra! A palavra era:",palavra_chave)
                        vencedor = nome_competidor
                        break
            elif opcao == "3":
                try:
                    ler_historico()
                except:
                    print("Arquivo não encontrado!")
                    print("É possível que não tenha nenhuma partida no histórico!")
            else:
                print("Opção inválida, tente novamente!")
            if erros >= 5:
                lose_upper = convert_caps(nome_competidor)
                print("Suas chances acabaram! " + lose_upper +" Você perdeu!")
                break                 

        opcao2 = menu_final()
        if opcao2 == "1":
            historico(nome_desafiante, nome_competidor, palavra_chave, vencedor)
            pass
        elif opcao2 == "2":
            historico(nome_desafiante, nome_competidor, palavra_chave, vencedor)
            break
        else:
            print("Opção inválida! O jogo foi reiniciado!")
            input("Press ENTER to continue...")
            pass
except:
    print("Algo de errado aconteceu! Por favor reinicie o jogo!")