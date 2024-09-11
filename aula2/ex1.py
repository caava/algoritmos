# faça um algoritmo quer lê 10 valores para uma variável do tipo lista
# de nome x e mostre os 10 valores armazenados

n = 10
x = []

for i in range(n):
    valor = input('Informe o valor desejado: ')
    x.append(valor)

for i in range(n):
    print(f'{i+1}° valor: {x[i]}')