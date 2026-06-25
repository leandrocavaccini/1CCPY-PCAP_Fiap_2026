#EXERCÍCIO 04

print("\n---Soma de 5 Números---\n")

soma = 0
contador = 0

while contador < 5:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1

print()

print(f"A soma é: {soma}")