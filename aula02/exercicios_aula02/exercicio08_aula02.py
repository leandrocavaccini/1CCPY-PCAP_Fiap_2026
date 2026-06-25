#EXERCÍCIO 08

print("\n---Calculadora de Troco de produtos---\n")

produto = str(input("Digite o nome do produto: "))
quantidade_produto = float(input(f"Digite a quantidade de {produto}(s) que vc quer: "))
valor_unitario_produto = float(input(f"Digite o valor unitário do(a) {produto}: "))
carteira = float(input("Digite o valor dado para a compra: "))

print()

valor_final = quantidade_produto * valor_unitario_produto

if carteira > valor_final:
    troco = carteira - valor_final
    print(f"Seu troco é de: R$ {troco}!")

elif valor_final > carteira:
    valor_faltante = valor_final - carteira
    print(f"Você deve: R$ {valor_faltante}!")

else:
    print(f"Tudo certinho, volte sempre!")