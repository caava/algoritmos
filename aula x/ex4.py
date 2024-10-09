# Faça um algoritmo que lê uma matriz M2X2 que calcula e mostra o resultado do determinante desta matriz.

import numpy as np

N = 2
m = []
lista = []

for i in range(N):
    for j in range(N):
        valor = int(input("Insira o valor: "))
        lista.append(valor)
    m.append(lista)
    lista = []

for i in range(N):
    for j in range(N):
        if m[i] == m[j]