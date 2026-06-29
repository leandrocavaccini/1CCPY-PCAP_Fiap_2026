#EXERCÍCIO 04

tamanho_vetor = int(input("Digite o número de indices no vetor: "))
print()

while tamanho_vetor <= 0:
    print("Digite um número inteiro e positivo!\n")
    tamanho_vetor = int(input("Digite o número de indices no vetor: "))
    print()

vetor_numeros = []

for i in range(tamanho_vetor):
    vetor_vetor_numeros = []
    numero = int(input(f"Número na {i + 1}º posição: "))
    vetor_vetor_numeros.append(numero)
    vetor_numeros.append(vetor_vetor_numeros)

somatorio = 0

for posicao in vetor_numeros:
    for soma in posicao:
        somatorio += soma

print()

print(f"O somatório dos números no vetor é: {somatorio}")