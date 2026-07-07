#EXERCÍCIO 05

print("\n---Fazendo uma Lista de Nomes Ficar Inversa---\n")

vetor_nomes = []

nome = input("Digite um nome: ")
vetor_nomes.append(nome)

while nome != "":
    nome = input("Digite um nome: ")
    vetor_nomes.append(nome)

if nome == "":
    vetor_nomes.remove(nome)

print()

print("Lista Invertida:")

print()

for i in range(len(vetor_nomes) - 1, -1, -1):
    print(vetor_nomes[i])