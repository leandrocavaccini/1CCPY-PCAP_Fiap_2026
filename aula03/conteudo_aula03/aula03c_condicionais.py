# RELACIONAIS
idade = float(input("Digite a idade: "))

maior_idade = idade >= 18

if maior_idade:
    print("Pode entrar")
else:
    print("Vaza daqui!!!")

#OPERADORES LÓGICOS
#AND, OR, NOT
verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Tu é burro ein, tenta de novo")

#NOTAS
print() # pular uma linha
nota_final = float(input("Digite a nota: "))

if nota_final < 4:
    print("Reprovado")

elif nota_final < 6:
    print("Reprovado")
else:
    print("Aprovado")

print("FIM")