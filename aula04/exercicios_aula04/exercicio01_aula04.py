#EXERCÍCIO 01

print("\n---Repetidor de Mensagens---\n")

print("---Olá Mundo---\n")

exibicao = input("Exibir mensagem novamente? s/n ")

print()

while exibicao == "s":
    print("---Olá Mundo---\n")
    exibicao = input("Exibir mensagem novamente? s/n ")
    print()

if exibicao == "n":
    print("---Fim---")

if exibicao != "s" and exibicao != "n":
    print("---ERRO!---")