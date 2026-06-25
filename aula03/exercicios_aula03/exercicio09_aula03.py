#EXERCÍCIO 09

print("\n---Transporte Rodoviário---\n")

codigo_estado_origem = int(input("Digite o código do estado de Origem: "))

while codigo_estado_origem < 1 or codigo_estado_origem > 5:
    print("Código inválido, digite um número de 1 até 5")
    codigo_estado_origem = int(input("Digite o código do estado de Origem: "))

peso_caminhao = float(input("Digite o peso do caminhão em toneladas: "))

codigo_carga = int(input("Digite o código da carga: "))

while codigo_carga < 10 or codigo_carga > 40:
    print("Código inválido, digite um número de 10 até 40")
    codigo_carga = int(input("Digite o código da carga: "))

print()

conversao_peso = peso_caminhao * 1000

def preco_final_sem_imposto():
    if 10 <= codigo_carga <= 20:
        preco_final = conversao_peso * 100

    elif 21 <= codigo_carga <= 30:
        preco_final = conversao_peso * 250

    elif 31 <= codigo_carga <= 40:
        preco_final = conversao_peso * 340

    return preco_final

match codigo_estado_origem:
    case 1:
        imposto = 35/100
    case 2:
        imposto = 25/100
    case 3:
        imposto = 15/100
    case 4:
        imposto = 5/100
    case 5:
        imposto = 0

preco_imposto = preco_final_sem_imposto() * imposto
preco_final_com_imposto = preco_final_sem_imposto() + (preco_final_sem_imposto() * imposto)

print("---INFORMAÇÕES FINAIS---\n")
print(f"O peso do caminhão em quilos (kg) é de: {conversao_peso}kg")
print(f"O preço da carga sem imposto é de: R${preco_final_sem_imposto()}")
print(f"O valor do imposto é de {imposto * 100}%, que do preço da carga totaliza: R${preco_imposto}")
print(f"O valor final da carga é de: R${preco_final_com_imposto} ")