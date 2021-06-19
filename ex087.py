# Aprimore o desafio anterior, mostrando no final:
# [A] A soma de todos os valores pares digitados.
# [B] A soma de todos os valores da terceira coluna.
# [C] O maior valor da segunda linha.
matriz = list()
linha = list()
somaPar = 0
soma3col = 0
maior2lin = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor de [{i},{j}]: '))
        if n % 2 == 0:
            somaPar += n
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
print('-=' * 13, end='-')
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print()
print('-=' * 13, end='-')
print()
for i in range(0, 3):
    if matriz[1][i] > maior2lin:
        maior2lin = matriz[1][i]
    if matriz[i][2]:
        soma3col += matriz[i][2]
print(f'A soma de todos os valores pares é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {soma3col}.')
print(f'O maior valor da segunda linha é {maior2lin}.')

