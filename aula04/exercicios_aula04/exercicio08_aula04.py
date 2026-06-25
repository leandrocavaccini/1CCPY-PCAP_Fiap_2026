#EXERCÍCIO 08

print("\n---Exibindo Divisores---\n")

num = int(input("Até qual número você deseja exibir os divisores? "))

print()

for divisores in range(1, num + 1):
    if num % divisores == 0:
        print(divisores)