#EXERCÍCIO 01

print("---Vetor de Quantidade de Posições Desejadas com Números Aleatorios---")

import random

numero_posicoes = int(input("Digite o número de posições que deseja no vetor: "))

while numero_posicoes <= 0:
    print("O número precisa ser inteiro, positivo e diferente de 0")
    numero_posicoes = int(input("Digite o número de posições que deseja no vetor: "))
    continue

vetor = []

for i in range(numero_posicoes):
    numero_aleatorio = int(random.uniform(0, 1000))
    vetor.append(numero_aleatorio)

for i in range(numero_posicoes):
    print(f"Posição {i}: {vetor[i]}")