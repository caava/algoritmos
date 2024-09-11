# Faça um algoritmo que lê duas listas A e B com 5 elementos cada.
# Construir uma lista C, sendo este a junção das duas outras listas, ou seja, a lista C deverá conter 10 elementos.
# Mostre no final a lista C.

n = 5
a = []
b = []
c = []

for i in range(n):
    valor = int(input('Informe o valor desejado: '))
    a.append(valor)

for i in range(n):
    valor = int(input('Informe o valor desejado: '))
    b.append(valor)

c = a + b

for i in range(len(c)):
    print(f'{i+1}° valor: {c[i]}')