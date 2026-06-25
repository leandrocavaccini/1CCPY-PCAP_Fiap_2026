#EXERCÍCIO 03

print("\n---Calculadora de Tabuada---\n")

numero = float(input("Digite seu número: "))

print()

for i in range(0, 26):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")