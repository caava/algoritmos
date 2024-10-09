# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (MNxN).
# Leia os valores inteiros para preencher todas as posições de cada uma das matrizes,
# e calcule a SOMA das matrizes.

import numpy as np

N = int(input('Insira o valor de N: '))
lista = []
m1 = []
m2 = []
m3 = []

for i in range(N):
    for j in range(N):
        valor = int(input("Insira o valor: "))
        lista.append(valor)
    m1.append(lista)
    lista = []
    
for i in range(N):
    for j in range(N):
        valor = int(input("Insira o valor: "))
        lista.append(valor)
    m2.append(lista)
    lista = []

m3 = np.add(m1, m2)
    
for i in range(N):
    print(m3[i])