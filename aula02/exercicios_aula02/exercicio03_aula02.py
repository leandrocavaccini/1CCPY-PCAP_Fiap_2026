#EXERCÍCIO 03

print("\n---Lojinha---\n")
print("Livros: R$ 25,00; Canetas: R$ 5,00\n")

livros = float(input("Digite a quantidade de livros comprados: "))
canetas = float(input("Digite a quantidade de canetas compradas: "))

print()

total = (livros * 25) + (canetas * 5)

print(f"O total gasto foi de: R$ {total}")