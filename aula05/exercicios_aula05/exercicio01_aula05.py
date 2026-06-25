#EXERCÍCIO 01

print("\n---Vetor de Quantidade de Posições Desejadas com Números Aleatorios---\n")

import random

numero_posicoes = int(input("Digite o número de posições que deseja no vetor: "))

print()

while numero_posicoes <= 0:
    print("O número precisa ser inteiro, positivo e diferente de 0")
    numero_posicoes = int(input("Digite o número de posições que deseja no vetor: "))
    continue

vetor = []

for i in range(numero_posicoes):
    numero_aleatorio = int(random.uniform(0, 1000))
    vetor.append(numero_aleatorio)
    print(f"Posição {i + 1}: {vetor[i]}")