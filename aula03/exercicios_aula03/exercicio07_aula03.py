#EXERCÍCIO 07

print("\n---Saiba se seu voto é obrigatório em 2026---\n")

ano_nascimento = int(input("Ano de nascimento: "))

print()

if ano_nascimento >= 2008:
    print("Seu voto não é obrigatório")

elif 2007 >= ano_nascimento >= 1956:
    print("Seu voto é obrigatório")

elif ano_nascimento < 1956:
    print("Seu voto não é obrigatório")