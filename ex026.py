#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase:')).upper().strip()
print('A letra a aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posiçao {}'.format(frase.find('A')+1))
print('A ultima letra A apararece na posiçao {}'.format(frase.rfind('A')+1))