from funcoes import limpar_tela

limpar_tela()

palavra_chave = str(input("Palavra: "))
letras_descobertas = []

print("JOGO DA FORCA")

for i in range(0, len(palavra_chave)):
    letras_descobertas.append("*")

acertou = False

while acertou == False :
    letra = str(input("DIgite a letra: "))

    for i in range(0, len(palavra_chave)):
        if letra == palavra_chave[i]:
            letras_descobertas[i] = letra

        print(letras_descobertas[i])

    acertou == True

    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == "*":
            acertou = False
