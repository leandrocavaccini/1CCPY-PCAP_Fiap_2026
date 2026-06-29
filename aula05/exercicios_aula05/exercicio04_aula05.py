#EXERCÍCIO 04

tamanho_vetor = int(input("Digite o número de indices no vetor: "))
print()

while tamanho_vetor <= 0:
    print("Digite um número inteiro e positivo!\n")
    tamanho_vetor = int(input("Digite o número de indices no vetor: "))
    print()

vetor_numeros = []

for i in range(tamanho_vetor):
    numero = int(input(f"Número na {i + 1}º posição: "))
    vetor_numeros.append(numero)

print()

print(f"O somatório dos números no vetor é: {sum(vetor_numeros)}")