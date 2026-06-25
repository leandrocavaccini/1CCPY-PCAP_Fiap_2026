#EXERCÍCIO 05

print("\n---Achando o Maior dos 5 Números---\n")

numero = float(input("Digite o 1º valor: "))
maior = numero
contador = 1

while contador < 5:
    proximo_numero = float(input(f"Digite o {contador + 1}º valor: "))

    if proximo_numero > maior:
        maior = proximo_numero

    contador += 1

print()

print(f"O maior valor digitado foi: {maior}")