print('olá mundo')

print(7 + 4)
print ('7 + 4')
print('7' + '4') # Concatenação de strings

# Comentário de linha de python
'''
Comentários
de
múltiplas
linhas
'''

# Variáveis

nome = 'Leandro'
idade = 26
peso = 75

print(nome, idade, peso)
print(f'oiiii, {nome}!!!!')

# Inputs - simulação de forms no cmd

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print('Oiiii', nome, '! Vc tem', idade, 'anos') #Ruim
print(f'Oiiii {nome} vc tem {idade} anos')

nova_idade = idade + 1
print(nova_idade)