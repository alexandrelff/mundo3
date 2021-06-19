# Crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta
matriz = list()
linha = list()
for i in range(0, 3):
    for j in range(0, 3):
        linha.append(int(input(f'Digite o valor de [{i},{j}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-=' * 13, end='-')
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print()
