# cálculo das médias com notas digitadas

# é preciso iniciar com zeros(0) neste caso
notas = [0, 0, 0, 0, 0] 
soma = 0
x = 0

# precisamos de estrutura de repetição para percorrer cada posição da lista
while x < 5: 
    notas[x] = float(input(f'Nota {x}: '))
    # atribuindo valores float para a lista
    soma += notas[x]
    x = x + 1
x = 0

# exibindo o conteúdo de cada posição da lista
while x < 5:
    print(f'Nota {x}: {notas[x]:6.2f}')
    x += 1
print(f'Média: {soma/x:5.2f}')

# outras formas de4 adicionar elementos a lista:
notas += [2] 
notas = notas + [2]

# para removermos um elemento da lista podemos utilizar a instrução del;
del notas[1]

# podemos apagar também fatias da lista:
del notas[1:99] # restaria Z = [0, 99, 100]