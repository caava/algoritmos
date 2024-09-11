# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x.
# Após completar toda a leitura da lista, verificar se cada valor armazenado na lista é par ou ímpar.
# Se for par, fazer com que o valor seja atualizado para o resultado da multiplicação do valor contido pelo índice.
# Se for impar, fazer com que a lista receba o valor do seu próprio índice.

n = 10
x = []


for i in range(n):
    valor = int(input('Informe o valor desejado: '))
    x.append(valor)

for i in range(n):
    if x[i] % 2 == 0:
        x[i] = x[i] * i
    else:
        x[i] = i

for i in range(n):
    print(f'{i+1}° valor: {x[i]}')