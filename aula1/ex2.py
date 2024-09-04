# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o somatório de todos os valores armazenados no vetor.

import numpy as np

n = 5

x = np.zeros(n)

for i in range(n):
    x[i] = float(input('Insira o valor desejado: '))

soma = x.sum()

print(f'A soma dos valores da lista é: {soma}')