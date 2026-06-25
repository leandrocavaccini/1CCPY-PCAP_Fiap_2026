#EXERCÍCIO 04

print("\n---Calculadora de aprovação (Média: 7.0)---\n")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

print()

mediaA = (nota1 + nota2 + nota3 + nota4) / 4

if mediaA >= 7:
    print(f"Sua média final é: {mediaA}")
    print("Aprovado")

elif 5 <= mediaA < 7:
    print(f" Sua média final é: {mediaA}")
    print("Recuperação")

elif mediaA < 5:
    print(f"Sua média final é: {mediaA}")
    print("Reprovado")