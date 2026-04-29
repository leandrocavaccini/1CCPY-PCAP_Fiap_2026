#EXERCÍCIO 02

print("---É Par ou Ímpar?---")

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"{num} é Par!")
else:
    print(f"{num} é Ímpar!")

#EXERCÍCIO 03

print("---Impressora de maior número---")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior")

elif num2 > num1:
    print(f"{num2} é maior")

elif num1 == num2:
    print("Os dois números são iguais!")

#EXERCÍCIO 04

print("---Calculadora de aprovação (Média: 7.0)---")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

mediaA = (nota1 + nota2 + nota3 + nota4) / 4

if mediaA >= 7:
    print(f"Sua média final é: {mediaA}")
    print("Aprovado")

elif mediaA >= 5 and mediaA < 7:
    print(f" Sua média final é: {mediaA}")
    print("Recuperação")

elif mediaA < 5:
    print(f"Sua média final é: {mediaA}")
    print("Reprovado")

#EXERCÍCIO 05

print("---Calculadora de Múltiplos---")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = num1 / num2

if num2 > num1:
    num3 = num2 / num1

if num3 % 1 == 0:
    print(f"{num1} e {num2} são múltiplos!")
else:
    print(f"{num1} e {num2} não são múltiplos")

#EXERCÍCIO 06

print("---Operações com caracteres (+,-,*,/)---")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
caractere = (input("Digite o caratere: "))

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

#EXERCÍCIO 07

print("---Saiba se seu voto é obrigatório em 2026---")

ano_nascimento = int(input("Ano de nascimento: "))

if ano_nascimento >= 2008:
    print("Seu voto não é obrigatório")

elif ano_nascimento <= 2007 and ano_nascimento >= 1956:
    print("Seu voto é obrigatório")

elif ano_nascimento < 1956:
    print("Seu voto não é obrigatório")

#EXERCÍCIO 08

print("---Reajuste de Salário---")

salario_antes = float(input("Digite o salário antes do reajuste: "))

if salario_antes <= 280:
    porcentagem = 20 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes
    print(f"Salário antes do reajuste: {salario_antes:.2f}")
    print(f"Porcentagem do reajuste: {porcentagem}")
    print(f"Aumento após reajuste: {aumento:.2f}")
    print(f"Salário depois do reajuste: {salario_depois:.2f}")

elif salario_antes > 280 and salario_antes <= 700:
    porcentagem = 15 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes
    print(f"Salário antes do reajuste: {salario_antes:.2f}")
    print(f"Porcentagem do reajuste: {porcentagem}")
    print(f"Aumento após reajuste: {aumento:.2f}")
    print(f"Salário depois do reajuste: {salario_depois:.2f}")

elif salario_antes > 700 and salario_antes < 1500:
    porcentagem = 10 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes
    print(f"Salário antes do reajuste: {salario_antes:.2f}")
    print(f"Porcentagem do reajuste: {porcentagem}")
    print(f"Aumento após reajuste: {aumento:.2f}")
    print(f"Salário depois do reajuste: {salario_depois:.2f}")

elif salario_antes >= 1500:
    porcentagem = 5 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes
    print(f"Salário antes do reajuste: {salario_antes:.2f}")
    print(f"Porcentagem do reajuste: {porcentagem}")
    print(f"Aumento após reajuste: {aumento:.2f}")
    print(f"Salário depois do reajuste: {salario_depois:.2f}")

#EXERCÍCIO 09
