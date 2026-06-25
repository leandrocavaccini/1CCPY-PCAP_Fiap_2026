#EXERCÍCIO 08

print("\n---Reajuste de Salário---\n")

salario_antes = float(input("Digite o salário antes do reajuste: "))

print()

porcentagem = 0
aumento = 0
salario_depois = 0

if salario_antes <= 280:
    porcentagem = 20 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes

elif 280 < salario_antes <= 700:
    porcentagem = 15 / 100
    salario_depois = salario_antes + (salario_antes * porcentagem)
    aumento = salario_depois - salario_antes

elif 700 < salario_antes < 1500:
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