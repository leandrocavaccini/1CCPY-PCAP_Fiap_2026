#EXERCÍCIO 06

print("\n---Operações com caracteres (+,-,*,/)---\n")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
caractere = (input("Digite o caratere: "))

print()

if caractere == "+":
    soma = num1 + num2
    print(f"Soma: {soma}")

elif caractere == "-":
    subtracao = num1 - num2
    print(f"Subtração: {subtracao}")

elif caractere == "*":
    multiplicacao = num1 * num2
    print(f"Multiplicação: {multiplicacao}")

elif caractere == "/":
    divisao = num1 / num2
    print(f"Divisão: {divisao}")

elif caractere != "+" or "-" or "*" or "/":
    print("ERRO")