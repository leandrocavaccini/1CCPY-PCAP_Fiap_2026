#EXERCÍCIO 01

print("---Repetidor de Mensagens---")

print("---Olá Mundo---")

exibicao = input("Exibir mensagem novamente? s/n ")

while exibicao == "s":
    print("---Olá Mundo---")
    exibicao = input("Exibir mensagem novamente? s/n ")

if exibicao == "n":
    print("---Fim---")

if exibicao != "s" and exibicao != "n":
    print("---ERRO---")

print()

#EXERCÍCIO 02

print("---Contador de 10 em 10---")

for i in range(0, 101, 10):
    print(i)

print()

#EXERCÍCIO 03

print("---Calculadora de Tabuada---")

numero = float(input("Digite seu número: "))

for i in range(0, 26):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print()

#EXERCÍCIO 04

print("---Soma de 5 Números---")

soma = 0
contador = 0

while contador < 5:
    numero = float(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1

print(f"A soma é: {soma}")

print()

#EXERCÍCIO 05

print("---Achando o Maior Número")

numero = float(input("Digite o 1º valor: "))
maior = numero
contador = 1

while contador < 5:
    proximo_numero = float(input(f"Digite o {contador + 1}º valor: "))

    if proximo_numero > maior:
        maior = proximo_numero

    contador += 1

print(f"O maior valor digitado foi: {maior}")

print()

#EXERCÍCIO 06

print("---Achando os Pares---")

numero = int(input("Digite um número: "))

for i in range(2, numero + 1):
    if i % 2 == 0:
        print(i)

if numero == numero < 0:
    print("ERRO")

print()

#EXERCÍCIO 07

print("---Soma de Todos os Números até o Número Inteiro---")

numero = int(input("Digite até que número deseja somar: "))

while numero <= 0:
    print("ERRO")
    numero = int(input("Digite outro número: "))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma de 1 até {numero} é: {soma}")

print()

#EXERCÍCIO 08

print("---Exibindo Divisores---")

num = int(input("Até qual número você deseja exibir os divisores? "))

for divisores in range(1, num + 1):
    if num % divisores == 0:
        print(divisores)

print()

#EXERCÍCIO 09

print("---Exibindo Primos---")

for num in range(2, 2001):
    primo = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} é primo")