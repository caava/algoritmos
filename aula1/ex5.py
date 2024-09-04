# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor
# e mostre qual a posição está armazenado o maior e o menor valor no vetor.

import numpy as np

n = 5

x = np.zeros(n)

for i in range(n):
    x[i] = float(input('Insira o valor desejado: '))

argmax = x.argmax()
argmin = x.argmin()

print(f'O valor máximo informado está na posição {argmax} da lista \ne o argumento minimo está na posição {argmin}.')