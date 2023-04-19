from funcoes import limpar_tela

limpar_tela()

print("-="*20)
print("JOGO DA FORCA")
print("-="*20)
nome_desafiante = input("Nome do desafiante: ")
nome_competidor = input("Nome do competidor: ")

limpar_tela()

palavra_chave = input("Digite a palavra chave: ")
dica1 = input("Digite a dica 1: ")
dica2 = input("Digite a dica 2: ")
dica3 = input("Digite a dica 3: ")

limpar_tela()

print("A palavra chave contém", len(palavra_chave), "letras!")
input("clique 'enter' para continuar...")
limpar_tela()

jogo_dica = input("")