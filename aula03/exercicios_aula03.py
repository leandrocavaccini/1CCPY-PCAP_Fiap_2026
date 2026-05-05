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

elif salario_antes > 280 and salario_antes <= 700:
    porcentagem = 15 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes

elif salario_antes > 700 and salario_antes < 1500:
    porcentagem = 10 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes

elif salario_antes >= 1500:
    porcentagem = 5 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes

print(f"Salário antes do reajuste: {salario_antes:.2f}")
print(f"Porcentagem do reajuste: {porcentagem}")
print(f"Aumento após reajuste: {aumento:.2f}")
print(f"Salário depois do reajuste: {salario_depois:.2f}")

#EXERCÍCIO 09

print("---Transporte Rodoviário---")

codigo_estado_origem = int(input("Digite o código do estado de Origem: "))

while codigo_estado_origem < 1 or codigo_estado_origem > 5:
    print("Código inválido, digite um número de 1 até 5")
    codigo_estado_origem = int(input("Digite o código do estado de Origem: "))

peso_caminhao = float(input("Digite o peso do caminhão em toneladas: "))

codigo_carga = int(input("Digite o código da carga: "))

while codigo_carga < 10 or codigo_carga > 40:
    print("Código inválido, digite um número de 10 até 40")
    codigo_carga = int(input("Digite o código da carga: "))

conversao_peso = peso_caminhao * 1000

def preco_final_sem_imposto():
    if codigo_carga >= 10 or codigo_carga <= 20:
        preco_final_sem_imposto = conversao_peso * 100

    elif codigo_carga >= 21 or codigo_carga <= 30:
        preco_final_sem_imposto = conversao_peso * 250

    elif codigo_carga >= 31 or codigo_carga <= 40:
        preco_final_sem_imposto = conversao_peso * 340

    return preco_final_sem_imposto

match codigo_estado_origem:
    case 1:
        imposto = 35/100
    case 2:
        imposto = 25/100
    case 3:
        imposto = 15/100
    case 4:
        imposto = 5/100
    case 5:
        imposto = 1

preco_imposto = preco_final_sem_imposto() * imposto
preco_final_com_imposto = preco_final_sem_imposto() + (preco_final_sem_imposto() * imposto)

print("---INFORMAÇÕES FINAIS---")
print(f"O peso do caminhão em quilos (kg) é de: {conversao_peso}kg")
print(f"O preço da carga sem imposto é de: R${preco_final_sem_imposto()}")
print(f"O valor do imposto é de {imposto * 100}% que do preço da carga totaliza: R${preco_imposto}")
print(f"O valor final da carga é de: R${preco_final_com_imposto} ")

#EXERCÍCIO 10

print("---Classificando Triângulos---")

ladoA = float(input("Lado A do triângulo: "))
ladoB = float(input("Lado B do triângulo: "))
ladoC = float(input("Lado C do triângulo: "))

if ladoA == ladoB == ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA > ladoB == ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA == ladoB > ladoC:
    ordem_decrescente = ladoA, ladoB,  ladoC

elif ladoB > ladoA == ladoC:
    ordem_decrescente = ladoB, ladoA, ladoC

elif ladoB == ladoC > ladoA:
    ordem_decrescente = ladoB, ladoC, ladoA

elif ladoC > ladoA == ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoC == ladoA > ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoA > ladoB > ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA > ladoC > ladoB:
    ordem_decrescente = ladoA, ladoC, ladoB

elif ladoB > ladoA > ladoC:
    ordem_decrescente = ladoB, ladoA, ladoC

elif ladoB > ladoC > ladoA:
    ordem_decrescente = ladoB, ladoC, ladoA

elif ladoC > ladoA > ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoC > ladoB > ladoA:
    ordem_decrescente = ladoC, ladoB, ladoA

if ladoA >= (ladoB + ladoC):
    print(f"Não forma Triângulo")

if ladoA ** 2 == ((ladoB ** 2) + ( ladoC ** 2)):
    print(f"É um Triângulo Retângulo")

if ladoA ** 2 > ((ladoB ** 2) + ( ladoC ** 2)):
    print(f"É um Triângulo Obtusângulo")

if ladoA ** 2 < ((ladoB ** 2) + (ladoC ** 2)):
    print(f"É um Triângulo Acutângulo")

if ladoA == ladoB == ladoC:
    print(f"É um Triângulo Equilátero")

if ladoA > ladoB == ladoC:
    print(f"É um Triângulo Isóceles")

if ladoA == ladoB > ladoC:
    print(f"É um Triângulo Isóceles")

if ladoB > ladoA == ladoC:
    print(f"É um Triângulo Isóceles")

if ladoB == ladoC > ladoA:
    print(f"É um Triângulo Isóceles")

if ladoC > ladoA == ladoB:
    print(f"É um Triângulo Isóceles")

if ladoC == ladoA > ladoB:
    print(f"É um Triângulo Isóceles")