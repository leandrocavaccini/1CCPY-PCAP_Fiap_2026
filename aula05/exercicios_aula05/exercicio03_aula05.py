#EXERCÍCIO 03

print("\n---Quantidade de Dias por Mês de Acordo com o Ano---\n")

ano = int(input("Digite o ano que deseja consultar: "))

print()

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

quantidade_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (ano % 4 == 0 and ano % 100 != 0) or ( ano % 400 == 0):
    print(f"O ano {ano} é bisexto, Fevereiro terá 29 dias!\n")
    quantidade_dias[1] = 29
else:
    print(f"O ano {ano} não é bisexto!\n")

for i in range(len(meses)):
    print(f"Mês: {meses[i]}, quantidade de dias: {quantidade_dias[i]}")