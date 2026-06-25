#EXERCÍCIO 04

print("\n---Calculadora de Velocidade Média---\n")

variacao_distancia = float(input("Digite a Variação de Distância: "))
variacao_tempo = float(input("Digite a Variação de Tempo: "))

print()

if variacao_distancia == 0:
    velocidade_media = float(input("Digite a Velocidade Média: "))
    variacao_distancia = (velocidade_media * variacao_tempo)
    print(f"A Variação de Distância é: {variacao_distancia:.2f}")

elif variacao_tempo == 0:
    velocidade_media = float(input("Digite a Velocidade Média: "))
    variacao_tempo = (variacao_distancia / velocidade_media)
    print(f"A Variação de Tempo é: {variacao_tempo:.2f}")

else:
    velocidade_media = (variacao_distancia / variacao_tempo)
    print(f"A Velocidade Média é: {velocidade_media:.2f}")