#EXERCÍCIO 01

print("---Calculadora de Área de Círculo---")

pi = 3.14159
raio = float(input("Digite o valor do raio: "))
area_circulo = pi * (raio ** 2)

print(f"A área do círculo é: {area_circulo:.2f}")

print()

#EXERCÍCIO 02

print("---Conversão de temperaturas---")

temperatura_fahrenheint = float(input("Digite a temperatura em fahrenheit: "))
temperatura_celcius = (temperatura_fahrenheint - 32) * 5/9

print(f"A temperatura em Celcius é: {temperatura_celcius:.2f}")

print()

#EXERCÍCIO 03

print("---Lojinha---")
print("Livros: R$ 25,00; Canetas: R$ 5,00")

livros = float(input("Digite a quantidade de livros comprados: "))
canetas = float(input("Digite a quantidade de canetas compradas: "))
total = (livros * 25) + (canetas * 5)

print(f"O total gasto foi de: R$ {total}")

print()

#EXERCÍCIO 04

print("---Calculadora de Velocidade Média---")

variacao_distancia = float(input("Digite a Variação de Distância: "))
variacao_tempo = float(input("Digite a Variação de Tempo: "))

if variacao_distancia == 0:
    velocidade_media = float(input("Digite a Velocidade Média: "))
    variacao_distancia = (velocidade_media * variacao_tempo)
    print(f"A Variação de Distância é: {variacao_distancia:.2f}")

elif variacao_tempo == 0:
    velocidade_media = float(input("Digite a Velocidade Média: "))
    variacao_tempo = (variacao_distancia / velocidade_media)
    print(f"A Variação de Tempo é: {variacao_tempo:.2f}")

else:
    velocidade_media = (variacao_distancia / variacao_tempo)
    print(f"A Velocidade Média é: {velocidade_media:.2f}")

print()

#EXERCÍCIO 05

print("---Calculadora de Média Aritmética---")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A Média Aritmética final do aluno é: {media:.2f}")

print()

#EXERCÍCIO 06

print("---Calculadora de Média Ponderada---")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media_ponderada = (((nota1 * 4) + (nota2 * 6)) / 10)

print(f"A Média Ponderada final do aluno é: {media_ponderada:.2f}")

print()

#EXERCÍCIO 07

print("---Calculadora de Valores de Peças---")

peca1 = str(input("Digite o nome da peça 1: "))
quantidade_peca1 = float(input(f"Digite a quantidade de {peca1}(s) que vc quer: "))
valor_unitario_peca1 = float(input(f"Digite o valor unitário do(a) {peca1}: "))

peca2 = str(input("Digite o nome da peça 2: "))
quantidade_peca2 = float(input(f"Digite a quantidade de {peca2}(s) que vc quer: "))
valor_unitario_peca2 = float(input(f"Digite o valor unitário do(a) {peca2}: "))

valor_final = (quantidade_peca1 * valor_unitario_peca1) + (quantidade_peca2 * valor_unitario_peca2)

print(f"A sua compra de {quantidade_peca1} {peca1}(s) e {quantidade_peca2} {peca2}(s) foi um total de: R$ {valor_final:.2f}")

print()

#EXERCÍCIO 08

print("---Calculadora de Troco de produtos---")

produto = str(input("Digite o nome do produto: "))
quantidade_produto = float(input(f"Digite a quantidade de {produto}(s) que vc quer: "))
valor_unitario_produto = float(input(f"Digite o valor unitário do(a) {produto}: "))
carteira = float(input("Digite o valor dado para a compra: "))
valor_final = quantidade_produto * valor_unitario_produto

if carteira > valor_final:
    troco = carteira - valor_final
    print(f"Seu troco é de: R$ {troco}")

elif valor_final > carteira:
    valor_faltante = valor_final - carteira
    print(f"Você deve: R$ {valor_faltante}")

else:
    print(f"Tudo certinho, volte sempre")