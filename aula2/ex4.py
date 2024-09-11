# Altere o algoritmo anterior para que ele realize o produto da primeira lista
# pelo inverso da segunda lista.

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

y.reverse()

for xa, ya in zip(x, y):
    z.append(xa * ya)

for i in range(n):
    print(f'{i+1}° valor: {z[i]}')
