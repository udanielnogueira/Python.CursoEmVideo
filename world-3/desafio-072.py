'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte

Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

x = int(input('Número de 0 a 20: '))

print(f'O número {x} por extenso é {numeros[x]}!')
