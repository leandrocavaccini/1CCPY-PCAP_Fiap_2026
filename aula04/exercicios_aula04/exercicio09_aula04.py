#EXERCÍCIO 09

print("\n---Exibindo Primos---\n")

numero = int(input("Até qual número deseja exibir os primos? "))

print()

print(f"Primos de 2 até {numero}\n")

for num in range(2, numero + 1):
    primo = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} é primo")