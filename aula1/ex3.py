# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine a média de todos os valores armazenados no vetor.

import numpy as np

n = 5

x = np.zeros(n)

for i in range(n):
    x[i] = float(input('Insira o valor desejado: '))

media = x.mean()

print(f'A média dos valores da lista é: {media}')