#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número'))
s = n + 1
a = n - 1
print('Analisando o número {} seu antecessor é {} e seu sucessor é {}'.format(n,(n-1),(n+1)))