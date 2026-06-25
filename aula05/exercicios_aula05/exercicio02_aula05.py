#EXERCÍCIO 02

print("\n---Calculando Média Semestral---\n")

numero_alunos = int(input("Digite quantos alunos tem na sala: "))

print()

while numero_alunos <= 0:
    print("O número de alunos tem que ser maior que 0")
    numero_alunos = int(input("Digite quantos alunos tem na sala: "))

vetor_notas = []

soma_notas = 0

print(f"Digite as notas dos {numero_alunos} alunos\n")

for i in range(numero_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    while nota < 0 or nota > 10:
        print("A nota tem que ser de 0 a 10")
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    vetor_notas.append(nota)
    soma_notas += nota

print()

vetor_notas.sort()
print(f"Notas em ordem crescente: {vetor_notas}\n")

media_semestral = sum(vetor_notas) / numero_alunos
print(f"A média semestral é: {media_semestral}\n")

acima_media = 0
na_media = 0
abaixo_media = 0

for i in range(numero_alunos):
    if vetor_notas[i] > media_semestral:
        acima_media += 1

    elif vetor_notas[i] == media_semestral:
        na_media += 1

    else:
        abaixo_media += 1

print(f"A quantidade de notas acima da média é: {acima_media}")
print(f"A quantidade de notas na média é: {na_media}")
print(f"A quantidade de notas abaixo da média é: {abaixo_media}")