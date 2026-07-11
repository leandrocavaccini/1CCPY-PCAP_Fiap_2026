#EXERCÍCIO 07

print("\n---Criando uma Matriz 3x4---\n")

import random

matriz = []

for i in range(0, 3):
    matriz_linhas = []
    matriz.append(matriz_linhas)
    for j in range(0, 4):
        matriz_linhas.append(random.randint(1, 10))

print("Matriz linear:\n")
print(matriz)

print()

print("Matriz montada:\n")
print(matriz[0])
print(matriz[1])
print(matriz[2])