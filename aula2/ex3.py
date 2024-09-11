# Elabore um algoritmo que leia duas listas de 5 posições
# após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.

n = 5
x = []
y = []
z = []

for i in range(n):
    valor = int(input('Informe o valor desejado: '))
    x.append(valor)

for i in range(n):
    valor = int(input('Informe o valor desejado: '))
    y.append(valor)

for xa, ya in zip(x, y):
    z.append(xa + ya)

for i in range(n):
    print(f'{i+1}° valor: {z[i]}')
