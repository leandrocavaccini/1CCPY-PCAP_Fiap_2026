#EXERCÍCIO 07

print("\n---Soma de Todos os Números até o Número Inteiro---\n")

numero = int(input("Digite até que número deseja somar: "))

print()

while numero <= 0:
    print("ERRO!")
    numero = int(input("Digite outro número: "))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma de 1 até {numero} é: {soma}")