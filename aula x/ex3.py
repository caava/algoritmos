# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável “a” (do tipo simples, pode ser: inteiro, float). 
# Multiplicar cada valor contido na matriz pelo valor da variável e colocar os resultados num vetor(lista) V com 16 elementos. 
# Mostre no final o vetor(lista).

N = 4
m = []
lista = []

for i in range(N):
    for j in range(N):
        valor = int(input("Insira o valor: "))
        lista.append(valor)
    m.append(lista)
    lista = []

a = float(input('Insira o valor da multiplicação: '))

for i in range(N):
    for j in range(N):
        lista.append(m[i][j]*a)

print(lista)