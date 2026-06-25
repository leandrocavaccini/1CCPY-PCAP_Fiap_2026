#EXERCÍCIO 10

print("\n---Classificando Triângulos---\n")

ladoA = float(input("Lado A do triângulo: "))
ladoB = float(input("Lado B do triângulo: "))
ladoC = float(input("Lado C do triângulo: "))

print()

if ladoA == ladoB == ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA > ladoB == ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA == ladoB > ladoC:
    ordem_decrescente = ladoA, ladoB,  ladoC

elif ladoB > ladoA == ladoC:
    ordem_decrescente = ladoB, ladoA, ladoC

elif ladoB == ladoC > ladoA:
    ordem_decrescente = ladoB, ladoC, ladoA

elif ladoC > ladoA == ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoC == ladoA > ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoA > ladoB > ladoC:
    ordem_decrescente = ladoA, ladoB, ladoC

elif ladoA > ladoC > ladoB:
    ordem_decrescente = ladoA, ladoC, ladoB

elif ladoB > ladoA > ladoC:
    ordem_decrescente = ladoB, ladoA, ladoC

elif ladoB > ladoC > ladoA:
    ordem_decrescente = ladoB, ladoC, ladoA

elif ladoC > ladoA > ladoB:
    ordem_decrescente = ladoC, ladoA, ladoB

elif ladoC > ladoB > ladoA:
    ordem_decrescente = ladoC, ladoB, ladoA

if ladoA >= (ladoB + ladoC):
    print(f"Não forma Triângulo")

if ladoA ** 2 == ((ladoB ** 2) + ( ladoC ** 2)):
    print(f"É um Triângulo Retângulo")

if ladoA ** 2 > ((ladoB ** 2) + ( ladoC ** 2)):
    print(f"É um Triângulo Obtusângulo")

if ladoA ** 2 < ((ladoB ** 2) + (ladoC ** 2)):
    print(f"É um Triângulo Acutângulo")

if ladoA == ladoB == ladoC:
    print(f"É um Triângulo Equilátero")

if ladoA > ladoB == ladoC:
    print(f"É um Triângulo Isóceles")

if ladoA == ladoB > ladoC:
    print(f"É um Triângulo Isóceles")

if ladoB > ladoA == ladoC:
    print(f"É um Triângulo Isóceles")

if ladoB == ladoC > ladoA:
    print(f"É um Triângulo Isóceles")

if ladoC > ladoA == ladoB:
    print(f"É um Triângulo Isóceles")

if ladoC == ladoA > ladoB:
    print(f"É um Triângulo Isóceles")