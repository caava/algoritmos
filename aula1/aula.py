import numpy as np

# define o tamanho do array
N = 5

# preeenche a estrutura com zeros
vetor = np.zeros(N)

# preenche o vetor com valores do tipo float
for i in range(N):
    vetor[i] = float(input(f'informe um valor para V[{i}]: '))

# outra forma de mostrar
for i in range(N):
    print(f'V[{i}] = {vetor[i]} ')

# mostra o tipo de estrutura
print(type(vetor))

soma = vetor.sum() # somatório
media = vetor.mean() # média
desvio = vetor.std() # desvio padrão
max = vetor.max() # o maior valor
min = vetor.min() # o menor valor
argmax = vetor.argmax() # retorna a posição que contém o maior valor da estrutura
argmin = vetor.argmin() # retorna a posição que contém o menor valor da estrutura