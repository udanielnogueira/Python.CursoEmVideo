'''
Crie um programa
qua leia o nome de uma
cidade e diga se ela
começa ou não com o
nome "SANTO".
'''

c = input('Digite o nome da cidade: ')

c = c.split()

print(c)

print('Começa com Santo?', c[0].upper() == 'SANTO')
