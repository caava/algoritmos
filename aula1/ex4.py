#Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o maior e o menor valor armazenado no vetor.

import numpy as np

n = 5

x = np.zeros(n)

for i in range(n):
    x[i] = float(input('Insira o valor desejado: '))

max = x.max()
min = x.min()

print(f'O valor máximo informado é: {max} \ne o valor mínimo é: {min}')