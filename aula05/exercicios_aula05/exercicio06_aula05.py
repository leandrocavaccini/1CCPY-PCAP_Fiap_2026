# EXERCÍCIO 06

print("\n---Trocando Posições de um Vetor---\n")

import random

quantidade_vetor = int(input("Digite quantas posições o vetor terá: "))

print()

while quantidade_vetor <= 0:
    print("Digite um valor válido!\n")
    quantidade_vetor = int(input("Digite quantas posições o vetor terá: "))
    print()

vetor = []

for i in range(quantidade_vetor):
    numero_aleatorio = int(random.uniform(0, 1000))
    vetor.append(numero_aleatorio)

print(vetor)

print("\nLista Invertida:\n")

for i in range(len(vetor) - 1, -1, -1):
    print(vetor[i])