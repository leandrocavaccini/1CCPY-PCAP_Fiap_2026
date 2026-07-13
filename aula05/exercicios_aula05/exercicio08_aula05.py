#EXERCÍCIO 08

print("\n---Somando Matrizes---\n")

import random

matriz_A = []

for i in range(0, 3):
    matriz_linhas_A = []
    matriz_A.append(matriz_linhas_A)
    for j in range(0, 4):
        matriz_linhas_A.append(random.randint(1, 10))

matriz_B = []

for i in range(0, 3):
    matriz_linhas_B = []
    matriz_B.append(matriz_linhas_B)
    for j in range(0, 4):
        matriz_linhas_B.append(random.randint(1, 10))

matriz_C = []

for i in range(0, 3):
    matriz_linhas_C = []
    matriz_C.append(matriz_linhas_C)
    for j in range(0, 4):
        matriz_linhas_C.append(matriz_A[i][j] + matriz_B[i][j])

print("Matrizes:\n")

print(f"Matriz A: {matriz_A}\n")

print(f"Matriz B: {matriz_B}\n")

print("Soma das Matrizes:\n")

print(f"Matriz C: {matriz_C}")