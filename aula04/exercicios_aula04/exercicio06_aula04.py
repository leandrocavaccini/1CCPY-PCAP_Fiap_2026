#EXERCÍCIO 06

print("\n---Achando os Pares---\n")

numero = int(input("Digite um número: "))

print()

for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)

if numero < 0:
    print("ERRO!")