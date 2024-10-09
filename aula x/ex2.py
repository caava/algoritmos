# Faça um algoritmo que lê uma matriz M10x10.
# Troque a seguir os valores contidos na linha de índice 2 com os da linha de índice 8 e também troque os valores da linha de índice 5 com os da coluna de índice 9.
# No final mostre a matriz.

N = 10
linha = []
m = []

for i in range(N):
    for j in range(N):
        valor = int(input(f"{i} Insira o valor {j}: "))
        linha.append(valor)
    m.append(linha)
    linha = []

for i in range(N):
    linha.append(m[2][i])
    m[2][i] = m[8][i]
    m[8][i] = linha[i]

linha = []

for i in range(N):
    linha.append(m[5][i])
    m[5][i] = m[i][9]
    m[i][9] = linha[i]

for i in range(N):
    print(m[i])