'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
a = input('Digite o nome do primeiro aluno')
b = input('Digite o nome do segundo aluno')
c = input('Digite o nome do terceiro aluno ')
d = input('Digite o nome do terceiro aluno')
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)
