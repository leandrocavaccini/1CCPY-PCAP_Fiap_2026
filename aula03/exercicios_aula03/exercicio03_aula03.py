#EXERCÍCIO 03

print("\n---Impressora de maior número---\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print()

if num1 > num2:
    print(f"{num1} é maior")

elif num2 > num1:
    print(f"{num2} é maior")

elif num1 == num2:
    print("Os dois números são iguais!")