#EXERCÍCIO 07

print("\n---Calculadora de Valores de Peças---\n")

peca1 = str(input("Digite o nome da peça 1: "))
quantidade_peca1 = float(input(f"Digite a quantidade de {peca1}(s) que vc quer: "))
valor_unitario_peca1 = float(input(f"Digite o valor unitário do(a) {peca1}: "))

print()

peca2 = str(input("Digite o nome da peça 2: "))
quantidade_peca2 = float(input(f"Digite a quantidade de {peca2}(s) que vc quer: "))
valor_unitario_peca2 = float(input(f"Digite o valor unitário do(a) {peca2}: "))

valor_final = (quantidade_peca1 * valor_unitario_peca1) + (quantidade_peca2 * valor_unitario_peca2)

print()

print(f"A sua compra de {quantidade_peca1} {peca1}(s) e {quantidade_peca2} {peca2}(s) foi um total de: R$ {valor_final:.2f}")