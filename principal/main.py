from funcoes import limpar_tela, tela_inicial, menu, historico, ler_historico, convert_caps

while True:
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

    limpar_tela()

    tamanho_palavra_chave = len(palavra_chave)
    palavra_oculta = '*' * tamanho_palavra_chave
    dicas_solicitadas = 0

    print("A palavra chave contém", tamanho_palavra_chave, "letra(s)!")
    input("Press ENTER to continue...")
    
    erros = 0
    tentativas = []
    acertos= []
    vencedor = []

    limpar_tela()

    while True:
        opcao = menu()
        if opcao =="2":
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
            pass
        elif opcao == "1":
            letra = input("Digite uma letra: ")
            if letra in tentativas:
                print("Você já tentou essa letra anteriormente.")
            elif letra not in palavra_chave:
                print("Essa letra não pertence a palavra.")
                tentativas.append(letra)
                erros += 1
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
        else:
            print("Opção inválida, tente novamente!")
        if erros >= 5:
            lose_upper = convert_caps(nome_competidor)
            print("Suas chances acabaram! " + lose_upper +" Você perdeu!")
            break                 
    
    opcao2 = input("\nMenu:\n(1)Jogar Novamente\n(2)Sair\n(3)Ver histórico de partidas\nEscolha uma opção: ")
    if opcao2 == "1":
        pass
    elif opcao2 == "2":
        break
    elif opcao2 == "3":
            try:
                historico(nome_desafiante, nome_competidor, palavra_chave, vencedor)
                ler_historico()
                input("Press ENTER to continue...")
            except:
                print("Arquivo não encontrado!")
    else:
        print("Opção inválida, tente novamente!")