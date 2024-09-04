# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor de nome x 
# e mostra os 10 valores armazenados na estrutura.

import numpy as np

n = 10

x = np.zeros(n)

for i in range(n):
    x[i] = float(input('Insira o valor desejado: '))

for i in range(n):
    print(f'{i+1}° valor: {x[i]}')
