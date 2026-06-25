#EXERCÍCIO 05

print("\n---Calculadora de Múltiplos---\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = num1 / num2

print()

if num2 > num1:
    num3 = num2 / num1

if num3 % 1 == 0:
    print(f"{num1} e {num2} são múltiplos!")
else:
    print(f"{num1} e {num2} não são múltiplos")