#EXERCÍCIO 06

print("\n---Calculadora de Média Ponderada---\n")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print()

media_ponderada = (((nota1 * 4) + (nota2 * 6)) / 10)

print(f"A Média Ponderada final do aluno é: {media_ponderada:.2f}")